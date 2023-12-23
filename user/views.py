from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import (PasswordChangeView, 
                                        PasswordResetView, 
                                        PasswordResetConfirmView, 
                                        LoginView)
from .forms import *
from .models import *
from blog.forms import BlogForm
from blog.models import BlogPostCategory, Blog

class UserCreateView(CreateView):
    template_name = 'register.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        new_password = form.cleaned_data.get('new_password')

        if new_password:
            user = form.save(commit=False)
            user.set_password(new_password)
            user.save()

            login(self.request, user)
            user.is_active = True
            user.last_login = timezone.now()
            user.save()

        return redirect('login')
    

def user_login(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']

            user = authenticate(request, phone=phone, password=password)
            if user is not None:
                login(request, user)
                return redirect('account')

            form.add_error(None, 'Yanlış nömrə və ya parol.')

    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form, 'title':'Daxil ol'})

UserModel = get_user_model()

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def update_form(request):
    
    account = request.user

    blogpostlari = Blog.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm_2(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UserProfileForm_2(instance=account)


    context = {
        'title':'Şəxsi Kabinet',
        'blogpostlari':blogpostlari
    }
    return render(request, "my-account.html", context)


@login_required
def meqale_elave_et(request):

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.user = request.user
            blog_post.save()
            print(blog_post)
            form.save_m2m()

            return redirect('meqale')
    else:
        form = BlogForm()
        

    context = {
        'title': 'Məqalə əlavə et',
        'form': form,
    }
    return render(request, "addblog.html", context)
from django.shortcuts import render, redirect
from blog.models import *
from .forms import *
from .models import *

# Create your views here.

def index(request):

    blogs_1 = Blog.objects.order_by("-created").all()


    context = {
        'title':'Xoş gəldin!',
        'blogs_1':blogs_1
    }

    return render(request, 'index.html', context=context)

def contact(request):
    
    meqaleelaqe = DeyisebilenContact.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'title':'Əlaqə',
        'form':form,
        'meqaleelaqe':meqaleelaqe,
    }
    return render(request, 'contact.html', context=context)

def haqqimizda(request):

    meqalehaqqimizda = DeyisebilenHaqqimizda.objects.first()

    context = {
        'title':'Haqqımızda',
        'meqalehaqqimizda':meqalehaqqimizda
    }

    return render(request, 'haqqimizda.html', context=context)
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .forms import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST

# Create your views here.

def blog(request, slug):
    blogdetail = get_object_or_404(Blog, slug=slug)
    comments = CommentPost.objects.all()
    user_comment = None
    if request.user.is_authenticated:
        user_comment = request.user
    
    if request.method == 'POST':
        form_2 = CommentForm(request.POST)
        if form_2.is_valid():
            comment = form_2.save(commit=False)
            comment.blogs = blogdetail
            comment.user_comment = user_comment

            if request.user.is_authenticated:
                comment.phone = request.user.phone  
                comment.name = request.user.first_name  

            comment.save()
            blogdetail.comment_count += 1
            blogdetail.save()
            return redirect('blog-etrafli', slug=blogdetail.slug)
    else:
        form_2 = CommentForm()

    try:
        blogdetail = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return redirect('error')

    blogdetail.read_count += 1
    blogdetail.save()
    blogs = Blog.objects.order_by("-created").all()
    title = blogdetail.title

    return render(request, 'blog.html', {'blogdetail': blogdetail, 'title': title, 'form_2':form_2, 'blogs':blogs,'comments':comments})

def commenti_sil(request):
    if request.method == 'POST' and request.user.is_authenticated:
        comment_id = request.POST.get('comment_id')
        try:
            comment = CommentPost.objects.get(id=comment_id, user_comment=request.user)
            blog = comment.blogs
            comment.delete()

            blog.comment_count = CommentPost.objects.filter(blogs=blog).count()
            blog.save()


            return JsonResponse({'success': True})
        except CommentPost.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Comment not found or not authorized.'})
    return JsonResponse({'success': False, 'message': 'Invalid request or user not authenticated.'})

def blog_2(request):
    categoryyy = BlogPostCategory.objects.all()
    blogs_1 = Blog.objects.order_by("-created").all()
    blogs = Blog.objects.order_by("-read_count").all()

    paginator = Paginator(blogs_1, 4)
    page_number = request.GET.get('page')
    sehifeler = paginator.get_page(page_number)

    context = {
        'title': 'Bloqlar',
        'blogs': blogs,
        'categoryyy':categoryyy,
        'sehifeler': sehifeler
    }
    return render(request, 'bloqlar.html', context=context)


def category_posts(request, slug):
    category = get_object_or_404(BlogPostCategory, slug=slug)
    categoryyy = BlogPostCategory.objects.all()
    posts = Blog.objects.filter(category=category)
    blogs = Blog.objects.all()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    sehifeler = paginator.get_page(page_number)

    context = {

        'title':category.title,
        'category': category,
        'posts': posts,
        'categoryyy':categoryyy,
        'sehifeler':sehifeler,
        }
    return render(request, 'category.html', context)


@require_POST
def like_post(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if request.user.is_authenticated:
        if request.user in blog.likes.all():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)

        blog.increment_likes_count()
    else:
        blog.increment_likes_count()

    return redirect('blog-etrafli', slug=blog.slug)


@require_POST
def dislike_post(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if request.user.is_authenticated:
        if request.user in blog.likes.all():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)

        blog.decrement_likes_count()
    else:
        blog.decrement_likes_count()

    return redirect('blog-etrafli', slug=blog.slug)
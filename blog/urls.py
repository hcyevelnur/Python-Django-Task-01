from django.urls import path, include
from . import views

urlpatterns = [
    path('blog-details/<slug:slug>/', views.blog, name='blog-etrafli'),
    path('commenti_sil/', views.commenti_sil, name='commenti_sil'),
    path('bloqlar', views.blog_2, name='bloqlar'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('like_post/<slug:slug>/', views.like_post, name='like_post'),
    path('dislike_post/<slug:slug>/', views.dislike_post, name='dislike_post'),

]
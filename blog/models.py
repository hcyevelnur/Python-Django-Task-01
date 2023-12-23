from django.db import models
from task01.utils.base import BaseModel
from django.utils.text import slugify
from user.models import *
# Create your models here.

class BlogPostTag(BaseModel):
    title = models.CharField(max_length=25, verbose_name='Tag adı: ')

    class Meta:
        verbose_name = 'Blog Post Tag'
        verbose_name_plural = 'Blog Post Tagləri'

    def __str__(self):
        return self.title


class BlogPostCategory(BaseModel):
    title = models.CharField(max_length=25, verbose_name='Kategoriya adı: ')
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, verbose_name="Slug:")


    class Meta:
        verbose_name = 'Blog Post Kateqoriya'
        verbose_name_plural = 'Blog Post Kateqoriyaları'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Like(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    blog_post = models.ForeignKey('blog.Blog', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Blog(BaseModel):
    blog_image = models.ImageField(upload_to='blog/', verbose_name='Bloq Şəkli')
    post_date = models.DateField(verbose_name='Tarix')
    title = models.CharField(max_length=255, verbose_name='Başlıq')
    blog_desc = models.TextField(verbose_name='Bloq Təsviri')
    tags = models.ManyToManyField('blog.BlogPostTag', related_name='product_tags', verbose_name='Tag adı:')
    read_count = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField('blog.BlogPostCategory', related_name='category', verbose_name='Kateqoriya:')
    comment_count = models.PositiveIntegerField(verbose_name='Şərh sayı', default=0)
    instagram = models.URLField(max_length=255, null=True, blank=True, verbose_name='Instagram URL')
    facebook = models.URLField(max_length=255, null=True, blank=True, verbose_name='Facebook URL')
    twitter = models.URLField(max_length=255, null=True, blank=True, verbose_name='Twitter URL')
    youtube = models.URLField(max_length=255, null=True, blank=True, verbose_name='YouTube URL')
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, verbose_name="Slug:")
    likes = models.ManyToManyField(UserModel, through=Like, related_name='liked_posts', blank=True)
    likes_count = models.PositiveIntegerField(default=0,null=True, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Blog Postu'
        verbose_name_plural = 'Bloq Postları'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def increment_likes_count(self):
        self.likes_count += 1
        self.save()

    def decrement_likes_count(self):
        self.likes_count -= 1
        self.save()

class CommentPost(BaseModel):
    comment_desc = models.TextField(verbose_name='Description')
    name = models.CharField(max_length=255, verbose_name='Name', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Phone', null=True, blank=True)
    blogs = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Blog', related_name='blogs', null=True, blank=True)
    user_comment = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='User:', related_name='comment_users', null=True, blank=True)

    class Meta:
        verbose_name = 'Commnet Post'
        verbose_name_plural = 'Commnet Posts'

    def __str__(self):
        return self.comment_desc
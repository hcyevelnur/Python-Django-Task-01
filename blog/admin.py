from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Blog)
admin.site.register(BlogPostCategory)
admin.site.register(BlogPostTag)
admin.site.register(CommentPost)
admin.site.register(Like)
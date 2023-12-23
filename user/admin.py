from django.contrib import admin
from .models import UserModel, UserProfile


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('phone', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('phone', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    readonly_fields = ('id',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    readonly_fields = ('id',)


admin.site.register(UserModel, UserModelAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import CustomUserManager

class UserModel(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=14, verbose_name='Phone', null=True, blank=True, default="", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name', null=True, blank=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'İstifadəçilər'
        verbose_name_plural = 'İstifadəçilər'

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name',null=True, blank=True)
    last_name = models.CharField(max_length=100, verbose_name='Last Name',null=True, blank=True)
    new_password = models.CharField(max_length=100, verbose_name='Password')
    confirm_password = models.CharField(max_length=100, verbose_name='Confirm Password')
    old_password = models.CharField(max_length=100, verbose_name='Confirm Password')
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='user_profile')

    def __str__(self):
        return self.first_name
    
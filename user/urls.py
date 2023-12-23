from django.urls import path
from . import views

urlpatterns = [
    path('qeydiyyat/', views.UserCreateView.as_view(), name='register'),
    path('daxil-ol/', views.user_login, name='login'),
    path('profil/', views.update_form, name='account'),
    path('meqale-elave-et/', views.meqale_elave_et, name='meqale'),
    path('logout/', views.user_logout, name='logout'),

]
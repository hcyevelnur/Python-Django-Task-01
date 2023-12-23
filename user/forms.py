from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.core import validators
from django.contrib.auth.forms import (UserCreationForm, 
                                    AuthenticationForm, 
                                    UsernameField, 
                                    PasswordChangeForm,
                                    PasswordResetForm,
                                    SetPasswordForm)

UserModel = get_user_model()

class UserProfileForm(forms.ModelForm):
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifrə', 'style': 'color: black;'}))
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Şifrəni təkrarla', 'style': 'color: black;'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adınız', 'style': 'color: black;'}))
    phone = forms.CharField(label='Telefon', min_length=13)

    class Meta:
        model = UserModel
        fields = ['phone','new_password', 'confirm_password', 'first_name',]
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if UserModel.objects.filter(phone=phone).exists():
            raise forms.ValidationError("Bu nömrə mövcuddur.")
        return phone

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if new_password != confirm_password:
            raise forms.ValidationError("Şifrələr uyğun gəlmir.")
        return confirm_password
    

class UserLoginForm(forms.Form):
    phone = forms.CharField(
        label='Telefon',
        min_length=13
    )
    password = forms.CharField(
        label='Şifrə',
        widget=forms.PasswordInput(attrs={'type': 'password', 'id': 'pass', 'class': 'form-control', 'placeholder': 'Şifrə', 'style': 'color: black;'})
    )

    def clean_email(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('Nömrə daxil edin')
        return phone

    def clean(self):
        phone = self.cleaned_data.get('phone')
        password = self.cleaned_data.get('password')
        user = UserModel.objects.filter(phone=phone).first()
        
        if not user:
            raise forms.ValidationError('Nömrə mövcud deyil')
        
        if not user.check_password(password):
            raise forms.ValidationError('Parol səhvdir.')

        return self.cleaned_data
    
class UserProfileForm_2(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'phone']

        widgets = {
            'first_name': 
            forms.TextInput(
                attrs={
                    'class': 'bg-bgray-50 dark:bg-darkblack-500 dark:text-white p-4 rounded-lg h-14 border-0 focus:border focus:ring-0',
                    'placeholder': 'Adınızı qeyd edin',}),
            'last_name': 
            forms.TextInput(
                attrs={
                    'class': 'bg-bgray-50 dark:bg-darkblack-500 dark:text-white p-4 rounded-lg h-14 border-0 focus:border focus:ring-0',
                      'placeholder': 'Soyadınızı qeyd edin', 'style': 'color: white;'}),
        }
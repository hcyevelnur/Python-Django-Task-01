from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone', 'email_address', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Adınız'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Soyadınız'}),
            'email_address': forms.EmailInput(attrs={'placeholder': 'E-Poçt'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'məs: 0501234567'}),
            'message': forms.Textarea(attrs={'class': 'mavi-border'}),
        }
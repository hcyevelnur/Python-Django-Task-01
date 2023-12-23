from django import forms
from .models import CommentPost, BlogPostTag, BlogPostCategory, Blog


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentPost
        fields = ['name', 'comment_desc', 'phone']

        widgets = {
            'name': forms.TextInput(attrs=({'class':'coment-field', 'placeholder':'Ad'})),
            'comment_desc': forms.Textarea(attrs=({'rows':'4','class':'form-control','placeholder':'Şərhiniz'})),
            'phone': forms.NumberInput(attrs=({'class':'coment-field','placeholder':'Phone'})),
        }

class BlogForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(queryset=BlogPostTag.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    category = forms.ModelMultipleChoiceField(queryset=BlogPostCategory.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Blog
        fields = [
            'blog_image', 'post_date', 'title', 'blog_desc', 'tags', 'category'
        ]

        widgets = {
            'post_date': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog_desc': forms.Textarea(attrs={'class': 'form-control'}),
        }
        

class BlogPostTagForm(forms.ModelForm):
    class Meta:
        model = BlogPostTag
        fields = ['title']

class BlogPostCategoryForm(forms.ModelForm):
    class Meta:
        model = BlogPostCategory
        fields = ['title', 'slug']
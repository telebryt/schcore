from django import forms
from .models import Post,Comments


class postform(forms.ModelForm):
    class Meta:
        model = Post
        fields =("author", "email", "title", "body","published","faculty")
        
class commentform(forms.ModelForm):
    class Meta:
        model = Comments
        fields =("name", "posts", "body", "active")
        
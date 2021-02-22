from django import forms
from .models import Post,Comments
from django.contrib.auth.models import User

class postform(forms.ModelForm):
    class Meta:
        model = Post
        fields =("author", "email", "title", "body","published","faculty")
        
class commentform(forms.ModelForm):
    class Meta:
        model = Comments
        fields =("name", "posts", "body", "active")
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ["first_name","last_name","email"]

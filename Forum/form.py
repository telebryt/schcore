from django import forms
from .models import PostModel,Comments
from django.contrib.auth.models import User

class postform(forms.ModelForm):
    class Meta:
<<<<<<< HEAD

        model = PostModel
        fields =("author", "email", "title", "content","status","faculty")

=======
        model = Post
        fields =("author", "title", "body","published","faculty")
>>>>>>> a990452d70a8d9bed15bae2a09bee1b658c252a8
        
class commentform(forms.ModelForm):
    class Meta:
        model = Comments
        fields =("name", "posts", "body", "active")
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ["first_name","last_name","email"]

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    def upload_location(instance, filename):
        return 'post/{filename}'.format(filename=filename)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to=upload_location, default="post/default.jpg")
    bio = models.TextField(blank=True,default="")
    phone = models.CharField(max_length=20, blank=True, default="")
    faculty = models.CharField(max_length=250,blank=True,default="")
    department = models.CharField(max_length=250, blank=True, default="")
    
    def create_profile(sender, *args, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfile(user=user)
            user_profile.save()

    post_save.connect(create_profile, sender=user)

    
    def __str__(self):
        return self.user


class Post(models.Model):
    Faculties = {
        ("University","University"),
        ("FOST", "FOST"),
        ("FOE", "FOE"),
        ("BUS", "BUS"),
        ("FAD", "FAD"),
        
    }
    status = {
        ("draft", "draft"),
        ("published", "published")
        
    }
    class PostManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(published="published")
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #email = models.EmailField( max_length=254)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250,unique_for_date = "published")
    body = models.TextField()
    published = models.CharField(max_length=50, choices=status,default="published")
    faculty = models.CharField(max_length=50, choices=Faculties,default="University")
    date_published = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()#default post manager
    PostManager = PostManager()#customer post manager

    class Meta:
        ordering = ['-date_published']
    def __str__(self):
        return 'comment {} by {} '.format(self.body, self.name)    

class Comments(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")
    parent = models.ForeignKey('self',null=True, on_delete=models.CASCADE,related_name="replies")
    body = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    active = models.BooleanField(default = False)
    
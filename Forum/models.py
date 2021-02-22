from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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
            return supper().get_queryset() .filter(status = "published")
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField( max_length=254)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250,unique_for_date = "published")
    body = models.TextField()
    published = models.CharField(max_length=50, choices=status,default="published")
    faculty = models.CharField(max_length=50, choices=Faculties,default="University")
    date_published = models.DateField(auto_now_add=True)
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
    
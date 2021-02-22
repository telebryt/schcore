from django.db import models
from django.template.defaultfilters import slugify
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


class PostModel(models.Model):
    class PostManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status = "Published")

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
    def upload_location(instance, filename):
        return 'post/{filename}'.format(filename=filename)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    title = models.CharField(max_length=250)
    images = models.ImageField(_("Image"), upload_to=upload_location, default='post/default.jpeg')
    content = models.TextField()
    email = models.EmailField(max_length=254)
    slug = models.SlugField(max_length = 250, unique_for_date = "Published")
    Published = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250,choices = status,default = "Published")
    faculty = models.CharField(max_length=50, choices = Faculties, default = 'News')
    objects = models.Manager() #default manager
    PostManager = PostManager()#custom manager

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    class Meta:
        ordering = ("-Published",)  

class Comments(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ForeignKey(PostModel, on_delete=models.CASCADE,related_name="comments")
    parent = models.ForeignKey('self',null=True , on_delete=models.CASCADE,related_name="replies")
    body = models.TextField()
    datePosted = models.DateField(auto_now_add=True)
    active = models.BooleanField(default = False)
    
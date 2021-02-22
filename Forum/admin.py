from django.contrib import admin
from .models import PostModel,Comments,UserProfile

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "email", "title", "content","status","faculty","Published")
    list_filter = ("faculty", "status")
    search_fields = ("author", "email", "body")
   

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "posts", "body", "active","datePosted","parent")
    list_filter = ("active", "datePosted")
    search_fields = ("name", "email", "body")
    actions = ["approved_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
@admin.register(UserProfile)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "faculty", "department","phone")



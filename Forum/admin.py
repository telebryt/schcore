from django.contrib import admin
from .models import PostModel,Comments,UserProfile

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):

    list_display = ("author", "title", "body","published","faculty","date_published")
    list_filter = ("faculty", "published")
    search_fields = ("author", "body")


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



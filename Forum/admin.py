from django.contrib import admin
from .models import Post,Comments,UserProfile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "email", "title", "body","published","faculty","date_published")
    list_filter = ("faculty", "published")
    search_fields = ("author", "email", "body")


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "posts", "body", "active","date_posted","parent")
    list_filter = ("active", "date_posted")
    search_fields = ("name", "email", "body")
    actions = ["approved_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
@admin.register(UserProfile)
class PostAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "faculty", "department","phone")



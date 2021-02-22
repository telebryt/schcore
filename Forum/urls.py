from django.urls import path
from .views import detail_post

app_name = "forum"

urlpatterns = [
    path("<int:pk>/",detail_post,name = "postcomment")
]

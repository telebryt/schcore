from django.urls import path
from Forum.views import index, detail_post

app_name = "forum"

urlpatterns = [

	path('', index, name="home"),
    path("<int:pk>/",detail_post,name = "postcomment"),
]
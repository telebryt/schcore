from django.urls import path
from Forums.views import index, detail_post,edituserdetails #registration

app_name = "forum"

urlpatterns = [

	path('', index, name="home"),
    path("profile/<int:pk>/",edituserdetails,name = "profile"),
    path("<int:pk>/", detail_post, name="postcomment"),
    #path("accounts/register/", registration, name="register"),
    
]
from django.urls import path 
from django.contrib.auth import views as auth_views
from .views import *


app_name = 'user'

urlpatterns = [
	path('',login, name='login'),
	path('<path:next_url>', login, name='login'),
		# change password urls
	#path('password_change/',auth_views.PasswordChangeView.as_view(template_name='user/reset.html'),name='password_change'),
	#path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
	# reset password urls
	
	]
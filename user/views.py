from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
# Create your views here.
	#authenticator

def login(request,next_url):
	username = request.POST.get('username')
	password = request.POST.get('password')
	new_user = auth.authenticate(username=username,password=password)
	
	if new_user is not None:
		auth.login(request, new_user)
		user = new_user
		return redirect(next_url)
	else:
		messages.info(request, 'User not found')
		return redirect(next_url)


def register(request):
	success = False 
	msg=  "Couldnt create account"
	if request.method == 'POST':
	 	form = UserRegisterForm(request.POST)
	 	print(form)
	 	if form.is_valid():
	 		form.save()
	 		username= form.cleaned_data.get('username')
	 		msg= messages.success(request, f'Account created for {username}!')
	 		data = {
				'success': True,
				'msg':msg,
				'username':username,

			}
	 		return JsonResponse(data, safe=False)
	else:
		form= UserRegisterForm()
	data = {
		'success': success,
		'msg':msg,

	}
	print(data)
	return render(request, 'user/register.html', data)

def reset(request):
	return render(request, 'user/reset.html',{})

def validate_username(request):
	username = request.GET.get('username', None)
	print(username)
	value = 2
	data = {
		'is_taken': User.objects.filter(username__iexact=username).exists(),
		

	}
	print(data)
	return JsonResponse(data, safe=False)

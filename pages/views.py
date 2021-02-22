from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'index.html', {'category':'AskHTU'})

def post_detail(request):
	return render(request, 'detail.html', {})
from django.shortcuts import render

from django.contrib.auth.models import User


# Create your views here.

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'about.html')

def login_page(request):
	return render(request, 'Registration/login.html')



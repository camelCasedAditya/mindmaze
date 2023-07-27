from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import time

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			messages.success(request, ("There Was An Error Logging In, Try Again..."))	
			return render(request, 'authenticate/login.html', {})	


	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return redirect('login')

def register(request):
	if request.user.is_authenticated:
		messages.success(request, ('You are already logged in'))
		return redirect('dashboard')

	else:
		if request.method == "POST":
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data['username']
				password = form.cleaned_data['password1']
				user = authenticate(username=username, password=password)
				login(request, user)
				messages.success(request, ("Registration Successful"))
				return redirect('dashboard')

		else:
			form = UserCreationForm()
		return render(request, 'authenticate/register.html', {
			'form':form,
		})
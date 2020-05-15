from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method == 'POST':
		# User has info and wants an account now
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accountes/signup.html', {'error':'User name was already been taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				auth.login(request, user)
				return redirect('home')
		else:
			return render(request, 'accountes/signup.html', {'error':'Passwords must match'})
	else:
		# The user wants to enter info
		return render(request, 'accountes/signup.html', {})


def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'accountes/login.html', {'error':'User name or password is incorrect.'})
	else:
		return render(request, 'accountes/login.html', {})


def logout(request):
	# TODO Need to route to homepage
	# and dont forget to logout
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')

from django.shortcuts import render

def signup(request):
	render(request, 'accountes/signup.html', {})

def login(request):
	render(request, 'accountes/login.html', {})

def logout(request):
	# TODO Need to route to homepage
	# and dont forget to logout
	render(request, 'accountes/signup.html', {})
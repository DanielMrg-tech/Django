from django.shortcuts import render, redirect
# django login functions
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import RegistrationForm

# Create your views here.

def register_view(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == "POST":
        # manage info sent through the form, using POST REQUEST
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
from django.shortcuts import render, redirect
from .forms import RegisterForm # EditUserForm, ResetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("all"))
    else:
        form = RegisterForm()
    
    return render(request, "register/register_user.html", {'form':form})
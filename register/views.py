from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import *
#INSTALLY pip install django-csp
#instally pip install pip-audit
def register(request):
    if request.method == "POST":
        # Get form data
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number") 

        # Check if the username or email is already taken
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        elif User.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "phone_number is already registered.")
        else:
            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)
            profile = Profile(user=user, phone_number=phone_number)
            user.save()
            profile.save()
            return redirect("index1") 

    return render(request, "register/register.html", {})

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        try:
            if username.isdigit():
                profile = Profile.objects.get(phone_number=username)
                user = profile.user
                username = user.username
            else:
                user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect("index1")
            else:
                messages.error(request, "Invalid login credentials.")
        except Profile.DoesNotExist:
            messages.error(request, "Account not found.")

    return render(request, "register/login.html", {})

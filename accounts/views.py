from django.shortcuts import render

# Create your views here.


from django.db import models

# Create your models here.
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages




# User Registration
class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):

        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # Validate empty fields
        if not username or not email or not password:
            messages.error(request, 'All fields are required')
            return redirect('register')

        # Check password match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        # Check username
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        # Check email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Account created successfully')

        return redirect('login')


# User Login
class UserLoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Authenticate user
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        messages.error(request, 'Invalid username or password')

        return redirect('login')


# User Logout
class UserLogoutView(View):

    def post(self, request):

        logout(request)

        return redirect('login')


# User Profile
class ProfileView(LoginRequiredMixin, TemplateView):

    template_name = 'profile.html'
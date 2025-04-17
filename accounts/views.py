from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AdminSignupForm, AdminLoginForm

def admin_signup(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admin account created successfully!')
            return redirect('admin_login')
    else:
        form = AdminSignupForm()
    return render(request, 'accounts/admin_signup.html', {'form': form})

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('book_list')
            else:
                messages.error(request, 'Invalid email or password')
    else:
        form = AdminLoginForm()
    return render(request, 'accounts/admin_login.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')
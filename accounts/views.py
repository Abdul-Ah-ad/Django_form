from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, EditProfileForm
from django.contrib.auth.forms import AuthenticationForm

def signup_view(request):
    try:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('profile')
        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})
    except Exception as e:
        messages.error(request, f"Signup error: {e}")
        return redirect('signup')

def login_view(request):
    try:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    except Exception as e:
        messages.error(request, f"Login error: {e}")
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required
def edit_profile_view(request):
    try:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully.')
                return redirect('profile')
        else:
            form = EditProfileForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form': form})
    except Exception as e:
        messages.error(request, f"Error updating profile: {e}")
        return redirect('edit_profile')

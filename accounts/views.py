from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, EditProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  

def signup_view(request):
    try:
        if request.method == 'POST':
            form = SignupForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Account created successfully!")  # ✅ Added success message
                return redirect('profile')
            else:
                messages.error(request, "Please fix the errors below.")  # ✅ Inform user if form invalid
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
        user = request.user
        profile = user.profile

        if request.method == 'POST':
            form = EditProfileForm(request.POST, request.FILES, instance=user, profile=profile)
            if form.is_valid():
                form.save(user, profile)  # ✅ Use the new save method that handles both
                messages.success(request, 'Profile updated successfully.')
                return redirect('profile')
        else:
            form = EditProfileForm(instance=user, profile=profile)

        return render(request, 'accounts/edit_profile.html', {
            'form': form,
            'profile': profile
        })
    except Exception as e:
        messages.error(request, f"Error updating profile: {e}")
        return redirect('edit_profile')



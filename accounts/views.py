from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def login_signup(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')  # Redirect to a home page
            else:
                messages.error(request, 'Invalid username or password')
        elif 'signup' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')  # Redirect to login page
            else:
                messages.error(request, 'Error creating account')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/login_signup.html', {'form': form})

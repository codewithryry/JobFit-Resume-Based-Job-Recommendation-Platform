from django.shortcuts import render
from django.contrib.auth.decorators import login_required




def index(request):
    return render(request, 'recommendations/index.html')  

def about(request):
    return render(request, 'recommendations/about.html')

def jobs(request):
    return render(request, 'recommendations/jobs.html')

def contact(request):
    return render(request, 'recommendations/contact.html')

def jobdetails(request):
    return render(request, 'recommendations/job-details.html')

def blog(request):
    return render(request, 'recommendations/blog.html')

def blogdetails(request):
    return render(request, 'recommendations/blog-details.html')

    
def team(request):
    return render(request, 'recommendations/team.html')


def terms(request):
    return render(request, 'recommendations/terms.html')

def testimonials(request):
    return render(request, 'recommendations/testimonials.html')

def profile_view(request):
    return render(request, 'recommendations/profile.html')  # Create this template for profile

@login_required
def settings_view(request):
    return render(request, 'recommendations/settings.html')  # Create this template for settings

# Signup view
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validate passwords
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Create user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        except:
            messages.error(request, "Username already exists!")
            return redirect('signup')

    return render(request, 'accounts/signup.html')


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'accounts/login.html')


# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')

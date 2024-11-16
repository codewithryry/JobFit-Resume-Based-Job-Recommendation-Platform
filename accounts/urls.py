from django.urls import path
from .views import CustomLoginView, signup_view, profile_view
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_signup, name='login_signup'),
]

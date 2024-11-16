"""
URL configuration for job_recommendation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recommendations import views
from django.urls import path, include  # Add include here

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_site'),
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('jobs/', views.jobs, name='jobs'),  # Jobs page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('job-details/', views.jobdetails, name='jobdetails'),  # Job details page
    path('blog/', views.blog, name='blog'),  # Blog page
    path('blog-details/', views.blogdetails, name='blogdetails'),  # Blog details page
    path('team/', views.team, name='team'),  # Team page
    path('terms/', views.terms, name='terms'),  # Terms page
    path('testimonials/', views.testimonials, name='testimonials'),  # Testimonials page

    path('profile/', views.profile_view, name='profile'),  # Profile page
    path('settings/', views.settings_view, name='settings'),  # Settings page
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]


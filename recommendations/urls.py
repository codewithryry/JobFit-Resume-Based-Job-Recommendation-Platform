from django.urls import path
from django.contrib import admin
from . import views  # Import your views from the recommendations app
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('jobs/', views.jobs, name='jobs'),  # Jobs page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('job-details/', views.jobdetails, name='jobdetails'),  # Job details page
    path('blog/', views.blog, name='blog'),  # Blog page
    path('blog-details/', views.blogdetails, name='blogdetails'),  # Blog details page
    path('team/', views.team, name='team'),  # Team page
    path('terms/', views.terms, name='terms'),  # Terms page
    path('ttestimonials/', views.testimonials, name='testimonials'),  # Testimonials page
]

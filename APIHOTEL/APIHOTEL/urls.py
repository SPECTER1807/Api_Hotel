"""APIHOTEL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home.as_view(),name='index'),
    path('about.html',About.as_view(),name='about'),
    path('amenities.html',Amenities.as_view(),name='amenities'),
    path('bookings.html',Bookings.as_view(),name='bookings'),
    path('contact.html',Contact.as_view(),name='contact'),
    path('failed.html',Failed.as_view(),name='failed'),
    path('faqs.html',Faqs.as_view(),name='faqs'),
    path('gallery.html',Gallery.as_view(),name='gallery'),
    path('privacy-policy.html',Privacy.as_view(),name='privacy'),
    path('rooms',Rooms.as_view(),name='rooms'),
    path('success.html',Success.as_view(),name='success'),

    
]

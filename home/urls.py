from django.contrib import admin
from django.urls import path
from home import views
import home

urlpatterns = [
   path("", views.index, name='home'),
   path("about", views.about, name='about'),
   path("service", views.service, name='service'),
   path("contact", views.contact, name='contact'),



]
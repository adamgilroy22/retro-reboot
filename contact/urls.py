from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact-form', views.contact_form, name='contact-form'),
]

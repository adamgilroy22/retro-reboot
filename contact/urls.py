from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('send-form', views.contact_form, name='contact_form'),
    path('open-tickets', views.OpenTickets.as_view(), name='open_tickets'),
]

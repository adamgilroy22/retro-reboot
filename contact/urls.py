from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('send-form', views.contact_form, name='contact_form'),
    path('open-tickets', views.ViewOpenTickets.as_view(), name='open_tickets'),
    path('ticket/<int:pk>/close-ticket',
         views.CloseTicket.as_view(), name='close_ticket'),
]

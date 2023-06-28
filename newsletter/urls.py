from django.urls import path
from . import views

urlpatterns = [
    path('newsletter-signup', views.newsletter_signup,
         name='newsletter-signup'),
]

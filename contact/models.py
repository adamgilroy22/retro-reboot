from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    """
    Created when a user submits a form on the contact
    us page
    """
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)

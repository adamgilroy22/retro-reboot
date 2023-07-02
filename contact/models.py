from django.db import models
from django.utils import timezone


class Ticket(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    sent_at = models.DateTimeField(default=timezone.now)

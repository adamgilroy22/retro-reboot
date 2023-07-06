from .models import Ticket
from django import forms


class ContactForm(forms.ModelForm):
    """
    Create a new ticket from contact form
    using ticket model
    """
    class Meta:
        model = Ticket
        fields = ('name', 'email', 'message',)

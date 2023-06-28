from django import forms
from .models import NewsletterSignup


class NewsletterForm(forms.ModelForm):

    class Meta:
        model = NewsletterSignup
        fields = '__all__'

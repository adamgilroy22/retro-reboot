from django import forms
from .models import DiscountCode


class DiscountForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Discount Code',
    }), label='')

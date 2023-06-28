from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSignup
from .forms import NewsletterForm


def newsletter_signup(request):
    """ Join Newsletter mailing list """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            member = form.save()
            messages.info(request, 'Successfully joined our mailing list!')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, 'Failed to sign up. Please ensure the \
            form is valid.')
    else:
        form = NewsletterForm()

    context = {
        'newsletter_form': form,
    }

    return redirect(request.META.get('HTTP_REFERER', '/'))

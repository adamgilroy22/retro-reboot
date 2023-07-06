from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Ticket
from .forms import ContactForm


def contact(request):
    """
    A view to return the index page
    """
    form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)


def contact_form(request):
    """ Handle contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            messages.info(request, 'Message sent!')

            """Send the user a confirmation email"""
            user_email = ticket.email
            subject = render_to_string(
                'contact/contact_form_confirmation_subject.txt')
            body = render_to_string(
                'contact/contact_form_confirmation_body.txt',
                {'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email]
            )

            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send message. \
            Try again.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

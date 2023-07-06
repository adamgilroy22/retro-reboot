from django.shortcuts import render, redirect, reverse
from django.contrib import messages
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

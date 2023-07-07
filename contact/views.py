from django.shortcuts import render, redirect, reverse
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
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


class ViewOpenTickets(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    Display all open tickets in a list
    only accessible by an admin
    """

    def get(self, request, *args, **kwargs):

        open_tickets = Ticket.objects.filter(
            seen=False).order_by('-sent_at')

        paginator = Paginator(open_tickets, 5)
        page_num = request.GET.get('page')
        tickets = paginator.get_page(page_num)

        context = {
            'open_tickets': tickets,
        }

        return render(request, 'contact/open_tickets.html', context)

    def test_func(self):
        return self.request.user.is_superuser


class CloseTicket(LoginRequiredMixin, View):
    """
    Close open tickets from open ticket list
    """

    def post(self, request, pk, *args, **kwargs):
        ticket = Ticket.objects.get(pk=pk)

        if not ticket.seen:
            ticket.seen = True
            ticket.save()
            messages.info(request, 'Ticket closed!')
        else:
            messages.error(request, 'Error!')

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

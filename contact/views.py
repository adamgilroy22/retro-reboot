from django.shortcuts import render


def contact(request):
    """
    A view to return the index page
    """
    return render(request, 'contact/contact.html')

from django.shortcuts import render


def index(request):
    """
    A view to return the index page
    """
    return render(request, 'homepage/index.html')


def contact(request):
    """
    A view to return the index page
    """
    return render(request, 'homepage/contact.html')

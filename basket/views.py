from django.shortcuts import render


def view_basket(request):
    """
    A view to render shopping basket page
    """
    return render(request, 'basket/basket.html')

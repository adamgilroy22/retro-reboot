from django.shortcuts import (
    render, redirect, HttpResponse, reverse, get_object_or_404
)
from django.contrib import messages
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product
from discount_codes.forms import DiscountForm
from discount_codes.models import DiscountCode


def view_basket(request):
    """
    A view to render shopping basket page
    """

    context = {
        'discount_form': DiscountForm(),
    }

    return render(request, 'basket/basket.html', context)


def add_to_basket(request, item_id):
    """
    Add quantity of product to basket
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        if product.stock >= basket[item_id] + quantity:
            basket[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} quantity \
                    to {basket[item_id]}')
        else:
            messages.error(
                request, f'Error {product.name} has only \
                {product.stock} units left, you have {basket[item_id]} \
                    in your basket')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the quantity of the specified product
    to the specific amount
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        if quantity > product.stock:
            messages.error(
                request, f'Error {product.name} has only \
                {product.stock} units left')
        else:
            basket[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity \
                to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """
    Remove a product from the basket
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def get_discount_code(request, code):
    try:
        discount_code = DiscountCode.objects.get(code=code)
        messages.info(request, "Successfully added coupon")
        return discount_code.discount
    except ObjectDoesNotExist:
        messages.error(request, "This code does not exist")
        return redirect(reverse('view_basket'))


def add_discount(request, *args, **kwargs):
    discount_form = DiscountForm(request.POST or None)
    if discount_form.is_valid():
        code = discount_form.cleaned_data.get('code')
        discount_code = get_discount_code(request, code)
        return redirect(reverse('view_basket'))

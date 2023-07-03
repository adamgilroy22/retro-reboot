from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product
from . import views


def basket_contents(request):
    """
    Handle calculations for adding products to the basket
    and taking a percentage off the grand total if a discount
    code has been used
    """

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})
    discount = request.session.get('discount')

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    if discount:
        savings = ((grand_total/100) * discount)
        grand_total -= savings
    else:
        savings = 0

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount': discount,
        'savings': savings,
    }

    return context

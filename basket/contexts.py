from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product
from . import views

from discount_codes.forms import DiscountForm
from discount_codes.models import DiscountCode


def get_discount_code(request, code):
    try:
        discount_code = DiscountCode.objects.get(code=code)
        messages.info(request, "Successfully added coupon")
        return discount_code.discount
    except ObjectDoesNotExist:
        messages.error(request, "This code does not exist")
        return 0


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    discount_code = 0
    basket = request.session.get('basket', {})

    discount_form = DiscountForm(request.POST or None)
    if discount_form.is_valid():
        code = discount_form.cleaned_data.get('code')
        discount_code = get_discount_code(request, code)

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

    grand_total = delivery + total - discount_code

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount_form': DiscountForm(),
    }

    return context

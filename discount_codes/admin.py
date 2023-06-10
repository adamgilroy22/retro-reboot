from django.contrib import admin
from .models import *


class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'discount'
    )

    ordering = ('discount',)


admin.site.register(DiscountCode, DiscountCodeAdmin)

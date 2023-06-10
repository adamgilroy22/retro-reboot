from django.contrib import admin
from .models import *


class DiscountCodeAdmin(admin.ModelAdmin):
    ordering = ('discount',)


admin.site.register(DiscountCode, DiscountCodeAdmin)

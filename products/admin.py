from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'platform',
        'condition',
        'price',
        'image'
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    ordering = ('name',)


class PlatformAdmin(admin.ModelAdmin):
    ordering = ('name',)


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(Condition)

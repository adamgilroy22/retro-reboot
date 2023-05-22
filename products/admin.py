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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Condition)

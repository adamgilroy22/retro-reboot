from django.contrib import admin
from .models import *


class NewsletterMemberAdmin(admin.ModelAdmin):
    ordering = ('email',)


admin.site.register(NewsletterSignup, NewsletterMemberAdmin)

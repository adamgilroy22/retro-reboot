from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'sent_at', 'seen')
    search_fields = ('name', 'email', 'message')
    actions = ['mark_seen']

    def mark_seen(self, request, queryset):
        queryset.update(seen=True)

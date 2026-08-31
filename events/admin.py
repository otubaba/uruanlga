from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'event_type',
        'venue',
        'start_date',
        'featured'
    )

    list_filter = (
        'event_type',
        'featured'
    )

    search_fields = (
        'title',
        'description'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }
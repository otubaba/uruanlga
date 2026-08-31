from django.contrib import admin
from .models import ContactMessage, Department


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'subject',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
    )

    search_fields = (
        'name',
        'email',
        'subject'
    )


admin.site.register(Department)
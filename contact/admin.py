from django.contrib import admin

from contact.models import ContactModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name','company', 'message', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'company', 'phone']

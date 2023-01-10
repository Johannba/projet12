from django.contrib import admin
from event.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ("name","attendees",'date_updated',"notes","support_contact",)
    list_filter = ( 'date_created',"attendees",)
    search_fields = ("attendees",)


admin.site.register(Event,EventAdmin)
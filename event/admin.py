from django.contrib import admin
from event.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ("name", 'attendees','date_updated',)
    


admin.site.register(Event)
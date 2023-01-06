from rest_framework.serializers import ModelSerializer

from event.models import Event

class EventSerializer(ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'support_contact',
            'client',
            'date_created',
            'date_updated',
            'event_status',
            'attendees',
            'event_date',
            'notes'
        ]
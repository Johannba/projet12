from rest_framework.viewsets import ModelViewSet

from event.serializers import EventSerializer

from event.models import Event


class EventViewset(ModelViewSet):
      
      serializer_class = EventSerializer     

      def get_queryset(self):
            return Event.objects.all()
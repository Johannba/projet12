from event.models import Event
from rest_framework import viewsets
from rest_framework.response import Response

from event.serializers import EventSerializer
from event.permissions import IsEventOrManager


class EventViewset(viewsets.ModelViewSet):
    def list(self, request):
        is_support = request.user.role == "support_member"
        is_sales = request.user.role == "sales_member"
        if is_support:
            queryset = Event.objects.filter(support_contact=request.user)
        elif is_sales:
            queryset = Event.objects.filter(support_contact=request.user)
        else:
            queryset = Event.objects.all()

        serializer = EventSerializer(
            self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsEventOrManager,)
    filterset_fields = (
        "support_contact",
        "client",
    )

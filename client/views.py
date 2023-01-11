from client.models import Client
from rest_framework import viewsets
from rest_framework.response import Response

from client.serializers import ClientSerializer
from client.permissions import IsSalesContactOrManager

from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(viewsets.ModelViewSet):
    def list(self, request):
        is_sales = request.user.role == "sales_member"
        if is_sales:
            queryset = Client.objects.filter(sales_contact=request.user)
        else:
            queryset = Client.objects.all()

        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsSalesContactOrManager, )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("first_name", "last_name", "email")
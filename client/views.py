from django.shortcuts import render
from client.models import Client
from rest_framework.viewsets import ModelViewSet

from client.serializers import ClientSerializer


class ClientViewset(ModelViewSet):
      serializer_class = ClientSerializer     

      def get_queryset(self):
            return Client.objects.all()
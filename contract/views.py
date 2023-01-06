from rest_framework.viewsets import ModelViewSet
from contract.models import Contract

from contract.serializers import ContractSerializer

# Create your views here.


class ContractViewset(ModelViewSet):
      
      serializer_class = ContractSerializer     

      def get_queryset(self):
            return Contract.objects.all()
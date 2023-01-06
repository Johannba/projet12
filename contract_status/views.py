from rest_framework.viewsets import ModelViewSet
from contract_status.models import ContratStatus

from contract_status.serializers import ContractStatusSerializer

# Create your views here.


class ContractstatusViewset(ModelViewSet):
      
      serializer_class = ContractStatusSerializer     

      def get_queryset(self):
            return ContratStatus.objects.all()
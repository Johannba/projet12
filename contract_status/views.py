from contract_status.models import ContratStatus
from rest_framework import viewsets
from rest_framework.response import Response

from contract_status.serializers import ContractStatusSerializer
from contract_status.permissions import IsContractStatusOrManager
# Create your views here.


      
class ContractStatusViewset(viewsets.ModelViewSet):
    def list(self, request):
        is_sales = request.user.role == "sales_member"
        if is_sales:
            queryset = ContratStatus.objects.filter(contract_id=request.user)
        else:
            queryset = ContratStatus.objects.all()

        serializer = ContractStatusSerializer(queryset, many=True)
        return Response(serializer.data)

    queryset = ContratStatus.objects.all()
    serializer_class = ContractStatusSerializer
    http_method_names = ["get", "post", "put", "delete"]
    filterset_fields = ("first_name", "last_name", "email")
    permission_classes = (IsContractStatusOrManager, )
from contract.models import Contract
from rest_framework import viewsets
from rest_framework.response import Response

from contract.serializers import ContractSerializer
from contract.permissions import IsContractOrManager

# Create your views here.


      
class ContractViewset(viewsets.ModelViewSet):
    def list(self, request):
        is_sales = request.user.role == "sales_member"
        if is_sales:
            queryset = Contract.objects.filter(sales_contact=request.user)
        else:
            queryset = Contract.objects.all()

        serializer = ContractSerializer(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    http_method_names = ["get", "post", "put", "delete"]
    filterset_fields = ("sales_contact", "client", "status")
    permission_classes = (IsContractOrManager, )
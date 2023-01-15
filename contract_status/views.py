from contract_status.models import ContratStatus
from rest_framework import viewsets
from rest_framework.response import Response

from contract_status.serializers import ContractStatusSerializer
from contract_status.permissions import IsContractStatusOrManager


class ContractStatusViewset(viewsets.ModelViewSet):
    def list(self, request):
        is_sales = request.user.role == "sales_member"
        if is_sales:
            queryset = ContratStatus.objects.filter(contract_id=request.user)
        else:
            queryset = ContratStatus.objects.all()

        serializer = ContractStatusSerializer(
            self.filter_queryset(self.get_queryset()),
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    queryset = ContratStatus.objects.all()
    serializer_class = ContractStatusSerializer
    http_method_names = ["get", "post", "put", "delete"]
    filterset_fields = ("is_signed",)
    permission_classes = (IsContractStatusOrManager,)

from rest_framework.serializers import ModelSerializer

from contract.models import Contract


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            "id",
            "sales_contact",
            "client",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payment_due",
        ]

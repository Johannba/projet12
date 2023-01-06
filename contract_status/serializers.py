from rest_framework.serializers import ModelSerializer


from contract_status.models import ContratStatus


class ContractStatusSerializer(ModelSerializer):

    class Meta:
        model = ContratStatus
        fields = [
            'id',
            'contract_id',
            'is_signed', ]
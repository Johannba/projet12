from rest_framework.permissions import BasePermission
from contract_status.models import ContratStatus


class IsContractStatusOrManager(BasePermission):
    def has_permission(self, request, view):
        print(view.kwargs)
        is_sales = request.user.role == "sales_member"
        is_manager = request.user.role == "management_member"
        if "pk" in view.kwargs and is_sales:
            contract = ContratStatus.objects.get(pk=view.kwargs["pk"])
        elif "AttributeError" == "AnonymousUser":
            return contract.contract_id == request.user
        return is_sales or is_manager

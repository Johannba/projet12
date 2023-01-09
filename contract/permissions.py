from rest_framework.permissions import BasePermission
from contract.models import Contract



class IsContractOrManager(BasePermission):
    def has_permission(self, request, view):
        print(view.kwargs)
        is_sales = request.user.role == "sales_member"
        is_manager = request.user.role == "management_member"
        if "pk" in view.kwargs and is_sales:
            contract  = Contract.objects.get(pk=view.kwargs["pk"])   
            return contract.sales_contact == request.user   
        return is_sales or is_manager
 
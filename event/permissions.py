from rest_framework.permissions import BasePermission
from event.models import Event


class IsEventOrManager(BasePermission):
    def has_permission(self, request, view):
        print(view.kwargs)
        is_sales = request.user.role == "sales_member"
        is_manager = request.user.role == "management_member"
        is_support = request.user.role == "support_member"
        if "pk" in view.kwargs and is_support:
            event = Event.objects.get(pk=view.kwargs["pk"])
            return event.support_contact == request.user
        return is_sales or is_manager or is_support

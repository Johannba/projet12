from django.contrib import admin
from contract_status.models import ContratStatus


class ContractStatusAdmin(admin.ModelAdmin):
    list_display = ("sales_contact", 'client','status', 'date_updated', )
    list_filter = ('date_created',)
    search_fields = ("client",)

admin.site.register(ContratStatus)

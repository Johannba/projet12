from django.contrib import admin
from contract_status.models import ContratStatus



class ContractStatusAdmin(admin.ModelAdmin):
    list_display = ("contract_id", 'is_signed', )
    search_fields = ("client",)

admin.site.register(ContratStatus,ContractStatusAdmin)

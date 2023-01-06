from django.contrib import admin
from .models import Contract

class ContractAdmin(admin.ModelAdmin):
    list_display = ("sales_contact", 'client','status', 'date_updated', )
    list_filter = ('date_created',)
    search_fields = ("client",)

admin.site.register(Contract, ContractAdmin,)

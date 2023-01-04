from django.contrib import admin
from .models import Contract

class ContractAdmin(admin.ModelAdmin):
    list_display = ("sales_contact", 'client','status', )
    list_filter = ('date_created',)
    

admin.site.register(Contract, ContractAdmin,)

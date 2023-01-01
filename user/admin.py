from django.contrib import admin
from user.models import User
from client.models import Client
from contract.models import Contract
from contract_satus.models import ContratStatus


admin.site.register(User)
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(ContratStatus)
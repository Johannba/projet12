from django.contrib import admin
from client.models import Client



class ClientAdmin(admin.ModelAdmin):
    list_filter = ('email', 'last_name', 'date_created')


admin.site.register(Client, ClientAdmin) 
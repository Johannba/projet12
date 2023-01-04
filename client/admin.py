from django.contrib import admin
from client.models import Client



class ClientAdmin(admin.ModelAdmin):
    list_filter = ('email', 'last_name', 'date_created')
    list_display= ('last_name',)


admin.site.register(Client, ClientAdmin) 

admin.site.site_header = "Admin Manager "
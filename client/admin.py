from django.contrib import admin
from client.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_filter = ("email", "last_name", "date_created")
    list_display = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "company_name",
    )
    empty_value_display = "Inconnu"
    search_fields = ("company_name",)


admin.site.register(Client, ClientAdmin)

admin.site.site_header = "Admin Manager "

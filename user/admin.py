from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ("email", "role", "phone_number")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "role", "phone_number")


class UserAdmin(BaseUserAdmin):
    exclude = ("username",)
    list_display = (
        "email",
        "role",
        "id",
    )
    list_filter = ("role",)
    ordering = ("email",)
    search_fields = ("role",)
    fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "email",
                    "password",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "role", "phone_number"),
            },
        ),
    )


admin.site.register(User, UserAdmin)

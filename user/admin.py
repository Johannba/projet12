from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', )


class UserAdmin(BaseUserAdmin):

    list_display = ( 'email', "role",)
    list_filter = ('role',)
    ordering = ('email',)
    search_fields = ("role",)
  
    

admin.site.register(User, UserAdmin)



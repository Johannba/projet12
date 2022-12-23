from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    SALES = 'sales_member'
    MANAGEMENT = 'management_member'
    SUPPORT = 'support_member'
    ROLE_CHOICES = (
        (SALES, 'sales_member'),
        (MANAGEMENT, 'management_member'),
        (SUPPORT, 'support_member')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.email}'
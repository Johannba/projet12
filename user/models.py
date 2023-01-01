from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, role, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(
            email=email,
            password=password,
            role='management_member',
            **extra_fields
        )


class User(AbstractUser):

    SALES = 'sales_member'
    MANAGEMENT = 'management_member'
    SUPPORT = 'support_member'
    ROLE_CHOICES = (
        (SALES, 'sales_member'),
        (MANAGEMENT, 'management_member'),
        (SUPPORT, 'support_member')
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True, default=1)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'
    
    
    
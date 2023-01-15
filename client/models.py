from django.db import models
from datetime import datetime

from user.models import User


class Client(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    sales_contact = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="sales_contact"
    )

    class Meta:
        verbose_name = "Client"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def update_date(self):
        self.date_updated = datetime.now()

    def save(self, *args, **kwargs):
        self.update_date()
        return super(Client, self).save()

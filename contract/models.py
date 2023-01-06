from django.db import models
from user.models import User
from client.models import Client
from datetime import datetime


class Contract(models.Model):

    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=True)
    amount = models.FloatField(default=0.0)
    payment_due = models.DateTimeField(auto_now_add=False)


    class Meta:
        verbose_name = 'Contrat'

    def __str__(self):
        return f'{Client.objects.get(id=self.client.id)} {self.date_created}'

    def update_date(self):
        self.date_updated = datetime.now()
        
    def save(self, *args, **kwargs):
        self.update_date()
        return super(Contract, self).save()
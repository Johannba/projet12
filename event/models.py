from django.db import models
from contract_status.models import ContratStatus
from user.models import User
from client.models import Client


class Event(models.Model):

    name = models.CharField(max_length=30, null=True, blank=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    event_status = models.ForeignKey(to=ContratStatus, on_delete=models.CASCADE)

    attendees = models.IntegerField(default=0)
    event_date = models.DateTimeField(auto_now_add=False)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

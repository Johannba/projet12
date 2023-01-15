from django.db import models
from contract.models import Contract


class ContratStatus(models.Model):
    contract_id = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    is_signed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contrat status"

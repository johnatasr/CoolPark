from django.db import models


# Create your models here.
class Automobilie(models.Model):
    plate = models.CharField(
        'Placa Automóvel',
        max_length=8,
        null=False,
        blank=False
    )

    class Meta:
        app_label = 'automobilies'

    def __str__(self):
        return self.plate
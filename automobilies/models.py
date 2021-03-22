from django.db import models


# Create your models here.
class Automobilie(models.Model):
    plate = models.CharField("Auto Plate", max_length=8, null=False, blank=False)

    def __str__(self):
        return self.plate

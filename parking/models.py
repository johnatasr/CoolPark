from django.db import models
from django.core.cache import cache
from django.utils import timezone

from automobilies.models import Automobilie


# Create your models here.
class ParkingOcurrency(models.Model):
    time = models.CharField("Time elapsed", max_length=244, null=True, blank=True)
    entry = models.DateTimeField()
    exit = models.DateTimeField(null=True)
    paid = models.BooleanField(default=False)
    left = models.BooleanField(default=False)
    auto = models.ForeignKey(Automobilie, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Parking Ocurrery"
        verbose_name_plural = "Parking Ocurrencies"

    def save(self, *args, **kwargs):
        self.entry = timezone.now()
        return super(ParkingOcurrency, self).save(*args, **kwargs)


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def delete(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class Parking(SingletonModel):
    """ "
    Model base, representation of Parking
    """

    parking_ocurrencies = models.ManyToManyField(ParkingOcurrency, blank=True)

    class Meta:
        verbose_name = "Park"

    def __str__(self):
        return str(self.id)

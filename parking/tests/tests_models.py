from parking.models import Parking, ParkingOcurrency
from automobilies.models import Automobilie
from django.test import TestCase


class POTest(TestCase):
    """
    Tests of ParkingOcurrency in parking.models.py
    """

    def test_create_po(self):
        auto = Automobilie.objects.create(plate=f"ABC-1234")
        parking = ParkingOcurrency.objects.create(
            paid=False, left=False, time="24 Hours", auto=auto
        )
        parking.save()

        po = ParkingOcurrency.objects.filter(auto__plate="ABC-1234")
        self.assertEquals(po.exists(), True)

    def test_update_po(self):
        auto = Automobilie.objects.create(plate=f"ABC-1234")
        parking = ParkingOcurrency.objects.create(
            paid=False, left=False, time="24 Hours", auto=auto
        )
        parking.save()

        po = ParkingOcurrency.objects.filter(auto__plate="ABC-1234")
        po = po.first()
        po.paid = True
        po.left = True
        po.save()

        self.assertEquals(po.paid, True)
        self.assertEquals(po.left, True)

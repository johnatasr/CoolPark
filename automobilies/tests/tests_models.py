from automobilies.models import Automobilie
from django.test import TestCase


class AutomobilieModelTest(TestCase):
    """
    Tests of Automobilie in parking.models.py
    """

    def setUp(self):
        Automobilie.objects.create(
            plate="ABC-1234",
        )

    def test_create_auto(self):
        Automobilie.objects.create(
            plate="CCC-1234",
        )
        park = Automobilie.objects.all()
        self.assertEquals(park.count(), 2)

    def test_update_auto(self):
        Automobilie.objects.create(
            plate="CCC-1234",
        )
        auto = Automobilie.objects.get(plate="CCC-1234")
        auto.plate = "AAA-1111"
        auto.save()

        self.assertEquals(auto.plate, "AAA-1111")

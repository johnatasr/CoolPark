from parking.models import ParkingOcurrency as ParkingOcurrencyModel
from automobilies.models import Automobilie
from parking.entities import ParkingOcurrency
from parking.repository import ParkRepo
from django.test import TestCase


class ParkingRepoTestCase(TestCase):
    """
    Tests of ParkRepo in parking.repository.py
    """

    def setUp(self):
        self.auto = Automobilie.objects.create(plate="ABC-1234")
        self.auto.save()

        self.po_model = ParkingOcurrencyModel.objects.create(
            paid=False, left=False, auto=self.auto
        )
        self.po_model.save()

        self.po = ParkingOcurrency(paid=False, left=False, auto=self.auto)
        self.repo = ParkRepo()

    def test_get_or_create_park_model(self):
        park: object = self.repo.get_or_create_parking_base_model()
        self.assertIsInstance(park, object)

    def test_create_parking_ocurrency_model(self):
        po = {"paid": True, "left": False, "auto": Automobilie(plate="ABC-1234")}

        po_entity = self.repo.create_parking_ocurrency_entity(parking_ocurrency=po)
        self.assertIsInstance(po_entity, object)
        self.assertEquals(po_entity.paid, po["paid"])
        self.assertEquals(po_entity.left, po["left"])
        self.assertEquals(po_entity.auto_plate, po["auto"].plate)

    def test_create_parking_ocurrency_by_plate(self):
        po_entity = self.repo.create_parking_ocurrency_by_plate("ABC-1234")
        self.assertIsInstance(po_entity, object)
        self.assertEquals(po_entity.paid, False)
        self.assertEquals(po_entity.left, False)
        self.assertEquals(po_entity.auto_plate, "ABC-1234")

    def test_get_parking_ocurrency_by_id(self):
        po_searched = self.repo.get_parking_ocurrency_by_id(1)
        self.assertIsInstance(po_searched, object)
        self.assertEquals(po_searched.exists(), False)

    def test_get_historic_by_plate(self):
        self.repo.create_parking_ocurrency_by_plate("CBA-4444")
        self.repo.create_parking_ocurrency_by_plate("CBA-4444")
        historic = self.repo.get_historic_by_plate("CBA-4444")
        self.assertEquals(historic.count(), 2)
        self.assertEquals(historic[0]["paid"], False)
        self.assertEquals(historic[1]["paid"], False)

    def test_update_parking_ocurrency_checkout(self):
        po_model = ParkingOcurrencyModel.objects.create(
            paid=True, left=False, auto=self.auto
        )
        po_entity = self.repo.update_parking_ocurrency_checkout(parking=po_model)

        self.assertIsInstance(po_entity, object)
        self.assertEquals(po_entity.paid, True)
        self.assertEquals(po_entity.left, True)
        self.assertEquals(po_entity.auto_plate, "ABC-1234")

    def test_update_parking_ocurrency_pay(self):
        po_model = ParkingOcurrencyModel.objects.create(
            paid=False, left=False, auto=self.auto
        )

        po_entity = self.repo.update_parking_ocurrency_pay(parking=po_model)
        self.assertIsInstance(po_entity, object)
        self.assertEquals(po_entity.paid, True)
        self.assertEquals(po_entity.left, False)
        self.assertEquals(po_entity.auto_plate, "ABC-1234")

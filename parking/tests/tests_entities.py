from automobilies.entities import Automobilie
from django.test import TestCase
from datetime import datetime
from parking.entities import ParkingOcurrency


class ParkingOcurrencyEnttityTestCase(TestCase):
    """
    Tests of ParkingOcurrency in parking.entities.py
    """

    def setUp(self):
        self.po_one = ParkingOcurrency(
            paid=False, left=False, auto=Automobilie(plate="ABC-1234")
        )

        self.po_two = ParkingOcurrency(
            paid=True, left=True, auto=Automobilie(plate="CBA-4321")
        )

    def test_isistance_object(self):
        self.assertIsInstance(self.po_one, object)
        self.assertIsInstance(self.po_two, object)

    def test_atributes_values_po(self):
        po1 = {
            "id": 1,
            "paid": False,
            "left": False,
            "entry": datetime(2021, 6, 10),
            "exit": datetime(2021, 6, 11),
            "time": "24 hours",
            "auto": Automobilie(plate="CBA-4321"),
        }

        po2 = {
            "id": 2,
            "paid": False,
            "left": False,
            "entry": datetime(2021, 6, 10),
            "exit": datetime(2021, 6, 11),
            "time": "24 hours",
            "auto": Automobilie(plate="CBA-4321"),
        }

        self.po_one.set_id(1)
        self.po_one.set_entry(datetime(2021, 6, 10))
        self.po_one.set_exit(datetime(2021, 6, 11))
        self.po_one.set_time("24 hours")

        self.po_two.set_id(2)
        self.po_two.set_entry(datetime(2021, 6, 10))
        self.po_two.set_exit(datetime(2021, 6, 12))
        self.po_two.set_time("48 hours")

        self.assertEquals(self.po_one.id, 1)
        self.assertEquals(self.po_one.id, po1["id"])
        self.assertEquals(self.po_one.paid, False)
        self.assertEquals(self.po_one.paid, po1["paid"])
        self.assertEquals(self.po_one.left, False)
        self.assertEquals(self.po_one.left, po1["left"])
        self.assertEquals(self.po_one.entry, datetime(2021, 6, 10))
        self.assertEquals(self.po_one.entry, po1["entry"])
        self.assertEquals(self.po_one.exit, datetime(2021, 6, 11))
        self.assertEquals(self.po_one.exit, po1["exit"])
        self.assertEquals(self.po_one.time, "24 hours")
        self.assertEquals(self.po_one.time, po1["time"])

    def test_atributes_type_po(self):
        self.po_one.set_id(1)
        self.po_one.set_entry(datetime(2021, 6, 10))
        self.po_one.set_exit(datetime(2021, 6, 11))
        self.po_one.set_time("24 hours")

        self.assertIsInstance(self.po_one.id, int)
        self.assertIsInstance(self.po_one.paid, bool)
        self.assertIsInstance(self.po_one.left, bool)
        self.assertIsInstance(self.po_one.entry, object)
        self.assertIsInstance(self.po_one.exit, object)
        self.assertIsInstance(self.po_one.time, str)
        self.assertIsInstance(self.po_one.auto, object)

    def test_repr_class_po(self):

        repr: str = "Entity: ParkingOcurrency<id:1, time:24 hours, paid:False, left:False, auto:ABC-1234>"

        self.po_one.set_id(1)
        self.po_one.set_entry(datetime(2021, 6, 10))
        self.po_one.set_exit(datetime(2021, 6, 11))
        self.po_one.set_time("24 hours")

        self.assertEquals(self.po_one.__str__(), repr)

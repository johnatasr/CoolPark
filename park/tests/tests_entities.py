from django.test import TestCase
from typing import List
from datetime import datetime
from ..entities import ParkingOcurrency, Park
from typing import Type

class ParkingOcurrenvyEnttityTestCase(TestCase):
    """
    Tests of Entity Parking Ocurrency, every variables will be called 'po'
    to make more simpler our tests
    """

    def setUp(self):
        self.po_one = ParkingOcurrency(
            paid=False,
            left=False,
            auto=[]
        )

        self.po_two = ParkingOcurrency(
            paid=True,
            left=True,
            auto=[]
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
            "time": "24 Hours",
            "auto": []
        }

        po2 = {
            "id": 2,
            "paid": False,
            "left": False,
            "entry": datetime(2021, 6, 10),
            "exit": datetime(2021, 6, 11),
            "time": "24 Hours",
            "auto": []
        }

        self.po_one.set_id(1)
        self.po_one.set_entry(datetime(2021, 6, 10))
        self.po_one.set_exit(datetime(2021, 6, 11))
        self.po_one.set_time('24 hours')

        self.po_two.set_id(2)
        self.po_two.set_entry(datetime(2021, 6, 10))
        self.po_two.set_exit(datetime(2021, 6, 12))
        self.po_two.set_time('48 hours')

        self.assertEquals(self.po_one.id, 1)
        self.assertEquals(self.po_one.id, po1['id'])
        self.assertEquals(self.po_one.paid, False)
        self.assertEquals(self.po_one.paid, po1['paid'])
        self.assertEquals(self.po_one.left, False)
        self.assertEquals(self.po_one.left, po1['left'])
        self.assertEquals(self.po_one.entry, datetime(2021, 6, 10))
        self.assertEquals(self.po_one.entry, po1['entry'])
        self.assertEquals(self.po_one.exit, datetime(2021, 6, 11))
        self.assertEquals(self.po_one.exit, po1['exit'])
        self.assertEquals(self.po_one.time, "24 Hours")
        self.assertEquals(self.po_one.time, po1['time'])
        self.assertEquals(self.po_one.auto, [])
        self.assertEquals(self.po_one.auto, po1['auto'])

        self.assertNotEquals(self.po_two.id, 1)
        self.assertNotEquals(self.po_two.id, po2['id'])
        self.assertNotEquals(self.po_two.paid, False)
        self.assertNotEquals(self.po_two.paid, po2['paid'])
        self.assertNotEquals(self.po_two.left, False)
        self.assertNotEquals(self.po_two.left, po2['left'])
        self.assertNotEquals(self.po_two.entry, datetime(2021, 6, 10))
        self.assertNotEquals(self.po_two.entry, po2['entry'])
        self.assertNotEquals(self.po_two.exit, datetime(2021, 6, 11))
        self.assertNotEquals(self.po_two.exit, po2['exit'])
        self.assertNotEquals(self.po_two.time, "24 Hours")
        self.assertNotEquals(self.po_two.time, po2['time'])
        self.assertNotEquals(self.po_two.auto, [])
        self.assertNotEquals(self.po_two.auto, po2['auto'])


    def test_atributes_type_po(self):
        self.po_one.set_id(1)
        self.po_one.set_entry(datetime(2021, 6, 10))
        self.po_one.set_exit(datetime(2021, 6, 11))
        self.po_one.set_time('24 hours')

        self.assertIsInstance(self.po_one.id, int)
        self.assertIsInstance(self.po_one.paid, bool)
        self.assertIsInstance(self.po_one.left, bool)
        self.assertIsInstance(self.po_one.entry, Type[datetime])
        self.assertIsInstance(self.po_one.exit, Type[datetime])
        self.assertIsInstance(self.po_one.time, str)
        self.assertIsInstance(self.po_one.auto, list)

    def test_rep_class_po(self):
        self.assertEquals(self.po_one.exit, po1['exit'])
        self.assertEquals(self.po_one.time, "24 Hours")
        self.assertEquals(self.po_one.time, po1['time'])
        self.assertEquals(self.po_one.auto, [])
        self.assertEquals(self.po_one.auto, po1['auto'])
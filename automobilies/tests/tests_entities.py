from automobilies.entities import Automobilie
from django.test import TestCase


class AutomobilieEntityTestCase(TestCase):
    """
    Tests of Automobilie in automobilies.entities.py
    """

    def setUp(self):
        self.auto_one = Automobilie(plate="ABC-1234")

        self.auto_two = Automobilie(plate="CBA-4321")

    def test_isistance_object(self):
        self.assertIsInstance(self.auto_one, object)
        self.assertIsInstance(self.auto_two, object)

    def test_atributes_values_po(self):
        auto1 = {"id": 1, "plate": "ABC-1234"}

        auto2 = {"id": 2, "plate": "CBA-4321"}

        self.auto_one.set_id(1)
        self.auto_two.set_id(2)

        self.assertEquals(self.auto_one.id, 1)
        self.assertEquals(self.auto_one.id, auto1["id"])
        self.assertEquals(self.auto_one.plate, "ABC-1234")
        self.assertEquals(self.auto_one.plate, auto1["plate"])

        self.assertEquals(self.auto_two.id, 2)
        self.assertEquals(self.auto_two.id, auto2["id"])
        self.assertEquals(self.auto_two.plate, "CBA-4321")
        self.assertEquals(self.auto_two.plate, auto2["plate"])

    def test_atributes_type_po(self):
        self.auto_one.set_id(1)
        self.auto_two.set_id(2)

        self.assertIsInstance(self.auto_one.id, int)
        self.assertIsInstance(self.auto_one.plate, str)

        self.assertIsInstance(self.auto_two.id, int)
        self.assertIsInstance(self.auto_two.plate, str)

    def test_repr_class_po(self):
        self.auto_one.set_id(1)
        repr: str = "Entity: Automobilie<id:1,  plate:ABC-1234>"
        self.assertEquals(self.auto_one.__str__(), repr)

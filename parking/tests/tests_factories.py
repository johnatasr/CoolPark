from django.test import TestCase
from parking.factories import ParkFactory
import unittest


class ParkingFactoryTestCase(TestCase):
    """
    Tests of ParkFactory in parking.factories.py
    """

    def setUp(self):
        self.factory = ParkFactory

    def test_create_check_in_iterator(self):
        msg = self.factory.create_check_in_interator({"plate": "ABC-1234"})
        self.assertIsInstance(msg, dict)

    def test_create_check_out_iterator(self):
        self.factory.create_check_in_interator({"plate": "ABC-1234"})
        msg = self.factory.create_check_out_interator(1)
        self.assertIsInstance(msg, dict)

    def test_create_do_payment_iterator(self):
        self.factory.create_check_in_interator({"plate": "ABC-1234"})
        msg = self.factory.create_do_payment_interator(1)
        self.assertIsInstance(msg, dict)

    def test_create_historic_iterator(self):
        self.factory.create_check_in_interator({"plate": "ABC-1234"})
        msg = self.factory.create_historic_interator("ABC-1234")
        self.assertIsInstance(msg, list)

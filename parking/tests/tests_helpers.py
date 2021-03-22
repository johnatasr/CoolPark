from django.test import TestCase
from parking.helpers import ParkingHelpers
from typing import Any, Type
from datetime import datetime
from django.utils import timezone
import unittest


class ParkingHelpersTestCase(TestCase):
    """
    Tests of ParkingHelpers in parking.helpers.py
    """

    def setUp(self):
        self.helpers = ParkingHelpers

        self.start_time: Type[datetime] = datetime(2021, 3, 22)
        self.end_time: Type[datetime] = datetime(2021, 3, 23)

        self.mask = "[A-Z]{3}-[0-9]{4}\Z"

    def test_transform_date_checkout_type(self):
        details: str = self.helpers.transform_date_checkout(
            self.start_time, self.end_time
        )
        self.assertIsInstance(details, str)

    def test_transform_date_checkout_value(self):
        details: str = self.helpers.transform_date_checkout(
            self.start_time, self.end_time
        )
        self.assertEquals(details, "0 minute")

    def test_regex_validate_type(self):
        result = self.helpers.regex_validate("ABC-1234", self.mask)
        self.assertIsInstance(result, bool)

    def test_regex_validate_value(self):
        result = self.helpers.regex_validate("ABC-1234", self.mask)
        self.assertEquals(result, True)

    def test_get_today_type(self):
        result = self.helpers.get_today()
        self.assertIsInstance(result, datetime)



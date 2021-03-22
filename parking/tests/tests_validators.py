from parking.validators import ParkValidator
from configs.exceptions import InvalidPayloadException
from django.test import TestCase
import unittest


class ParkValidatorTestCase(TestCase):
    """
    Tests of ParkValidator in parking.validators.py
    """

    def setUp(self):
        self.validator = ParkValidator()

    def test_type_regex(self):
        self.assertEquals(self.validator.DEFAULT_PLATE_MASK, "[A-Z]{3}-[0-9]{4}\Z")

    def test_validate(self):
        self.assertEquals(self.validator.validate(True), True)
        self.assertEquals(self.validator.validate(False), False)

    def test_is_empty_payload(self):
        payload = {"plate": "ABC-1234"}
        result = self.validator.is_empty_payload(payload)
        self.assertEquals(result, True)

    def test_validate_only_plate(self):
        plate = "ABC-1234"
        result = self.validator.validate_only_plate(plate)
        self.assertEquals(result, True)

    def test_validate_payload(self):
        payload = {"plate": "ABC-1234"}
        result = self.validator.validate_payload(payload)
        self.assertEquals(result, True)

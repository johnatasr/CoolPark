from django.test import TestCase
from parking.iterators import (
    CheckInIterator,
    CheckOutIterator,
    DoPaymentIterator,
    HistoricIterator,
)
from parking.serializers import DefaultSerializer, HistoricSerializer
from parking.validators import ParkValidator
from parking.repository import ParkRepo


class CheckInIteratorTestCase(TestCase):
    """
    Tests of CheckInIterator in parking.iterator.py
    """

    def setUp(self):
        self.iterator = CheckInIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        )

    def test_init(self):
        self.assertIsInstance(self.iterator, object)
        self.assertIsInstance(self.iterator.validator, object)
        self.assertIsInstance(self.iterator.repo, object)
        self.assertIsInstance(self.iterator.serializer, object)

    def test_set_params(self):
        self.iterator.set_params(park_payload={"plate": "ABC-1234"})
        self.assertIsInstance(self.iterator.payload, dict)
        self.assertEquals(self.iterator.payload["plate"], "ABC-1234")

    def test_execute(self):
        result = self.iterator.set_params(park_payload={"plate": "ABC-1234"}).execute()
        self.assertIsInstance(result, dict)
        self.assertEquals(result["msg"], "Check-in created")
        self.assertEquals(result["plate"], "ABC-1234")


class CheckOutIteratorTestCase(TestCase):
    """
    Tests of CheckOutIterator in parking.iterator.py
    """

    def setUp(self):
        self.iterator = CheckOutIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        )

    def test_init(self):
        self.assertIsInstance(self.iterator, object)
        self.assertIsInstance(self.iterator.validator, object)
        self.assertIsInstance(self.iterator.repo, object)
        self.assertIsInstance(self.iterator.serializer, object)

    def test_set_params(self):
        self.iterator.set_params(1)
        self.assertIsInstance(self.iterator.parking_id, int)
        self.assertEquals(self.iterator.parking_id, 1)

        self.iterator.set_params("1")
        self.assertIsInstance(self.iterator.parking_id, str)
        self.assertEquals(self.iterator.parking_id, "1")

    def test_execute(self):
        check_in = CheckInIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params({"plate": "ABC-1234"}).execute()

        result = self.iterator.set_params(parking_id=6).execute()
        self.assertIsInstance(result, dict)

    def test_execute_payment_not_done(self):
        CheckInIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params({"plate": "ABC-1234"}).execute()

        result = self.iterator.set_params(1).execute()
        self.assertIsInstance(result["msg"], str)

    def test_execute_already_done(self):
        CheckInIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params({"plate": "ABC-1234"}).execute()

        DoPaymentIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params(1).execute()

        CheckOutIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params(1).execute()

        result = self.iterator.set_params(parking_id=1).execute()
        self.assertIsInstance(result["msg"], str)

    def test_execute_wrong_id(self):
        result = self.iterator.set_params(parking_id=48).execute()
        self.assertIsInstance(result["msg"], str)


class DoPaymentIteratorTestCase(TestCase):
    """
    Tests of DoPaymentIterator in parking.iterator.py
    """

    def setUp(self):
        self.iterator = DoPaymentIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        )

    def test_init(self):
        self.assertIsInstance(self.iterator, object)
        self.assertIsInstance(self.iterator.validator, object)
        self.assertIsInstance(self.iterator.repo, object)
        self.assertIsInstance(self.iterator.serializer, object)

    def test_set_params(self):
        self.iterator.set_params(1)
        self.assertIsInstance(self.iterator.parking_id, int)
        self.assertEquals(self.iterator.parking_id, 1)

        self.iterator.set_params("1")
        self.assertIsInstance(self.iterator.parking_id, str)
        self.assertEquals(self.iterator.parking_id, "1")

    def test_execute(self):
        CheckInIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params({"plate": "ABC-1234"}).execute()

        result = self.iterator.set_params(parking_id=1).execute()
        self.assertIsInstance(result, dict)

    def test_execute_payment_already(self):
        CheckInIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params({"plate": "ABC-1234"}).execute()

        DoPaymentIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params(1).execute()

        result = self.iterator.set_params(1).execute()
        self.assertIsInstance(result["msg"], str)

    def test_execute_wrong_id(self):
        result = self.iterator.set_params(48).execute()
        self.assertEquals(result["msg"], "Parking not found with ID : 48")


class HistoricIteratorTestCase(TestCase):
    """
    Tests of HistoricIterator in parking.iterator.py
    """

    def setUp(self):
        self.iterator = HistoricIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=HistoricSerializer
        )

    def test_init(self):
        self.assertIsInstance(self.iterator, object)
        self.assertIsInstance(self.iterator.validator, object)
        self.assertIsInstance(self.iterator.repo, object)
        self.assertIsInstance(self.iterator.serializer, object)

    def test_set_params(self):
        self.iterator.set_params(plate="ABC-1234")
        self.assertIsInstance(self.iterator.plate, str)
        self.assertEquals(self.iterator.plate, "ABC-1234")

    def test_execute(self):
        CheckInIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params({"plate": "ABC-1234"}).execute()

        DoPaymentIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params(1).execute()

        CheckOutIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params(1).execute()

        CheckInIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params({"plate": "ABC-1234"}).execute()

        DoPaymentIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params(2).execute()

        CheckOutIterator(
            validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
        ).set_params(2).execute()

        result = self.iterator.set_params(plate="ABC-1234").execute()
        self.assertIsInstance(result, list)
        self.assertEquals(len(result), 2)


    def test_execute_not_fould(self):
        result = self.iterator.set_params(plate="ASQ-1234").execute()
        self.assertEquals(result["msg"], "Historic not found with plate : ASQ-1234")

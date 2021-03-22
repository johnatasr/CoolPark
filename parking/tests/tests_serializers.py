from parking.entities import ParkingOcurrency
from parking.models import ParkingOcurrency as ParkingOcurrencyModel
from parking.serializers import DefaultSerializer, HistoricSerializer
from automobilies.models import Automobilie
from django.test import TestCase


class DefaultSerializerTestCase(TestCase):
    """
    Tests of DefaultSerializer in parking.serializer.py
    """

    def setUp(self):
        self.po = ParkingOcurrency(paid=False, left=False, auto=Automobilie("CBA-4321"))
        self.po.set_id(1)

        self.serializer = DefaultSerializer

    def test_init(self):
        serializer = self.serializer(parking=self.po, msg="Init test")
        self.assertIsInstance(serializer.parking, object)
        self.assertIsInstance(serializer.msg, str)

    def test_mount_payload(self):
        serializer = self.serializer(parking=self.po, msg="Mount test")
        dict_message = serializer.mount_payload()
        self.assertIsInstance(dict_message, dict)
        self.assertEquals(dict_message["id"], 1)
        self.assertEquals(dict_message["msg"], "Mount test")

    def test_create_message(self):
        serializer = self.serializer(parking=self.po, msg="Create message test")
        message = serializer.create_message()
        self.assertIsInstance(message, dict)


class HistoricSerializerTestCase(TestCase):
    """
    Tests of HistoricSerializerTestCase in parking.serializer.py
    """

    def setUp(self):
        self.serializer = HistoricSerializer

        auto = Automobilie.objects.create(plate="CBA-1234")
        auto.save()

        for i in range(1, 4):
            park = ParkingOcurrencyModel.objects.create(
                paid=True, left=True, time=f"3{i} minutes", auto=auto
            )
            park.save()

    def test_init(self):
        results = ParkingOcurrencyModel.objects.filter(auto__plate="CBA-1234")
        serializer = self.serializer(historic=results)
        self.assertIsInstance(serializer.historic, object)
        self.assertEquals(serializer.historic.count(), 3)

    def test_mount_payload(self):
        results = ParkingOcurrencyModel.objects.filter(auto__plate="CBA-1234").values(
            "id", "time", "paid", "left"
        )
        serializer = self.serializer(historic=results)
        list_historic = serializer.mount_payload()
        self.assertIsInstance(list_historic, list)
        self.assertEquals(list_historic[0]["time"], "31 minutes")
        self.assertEquals(list_historic[1]["time"], "32 minutes")

    def test_create_message(self):
        results = ParkingOcurrencyModel.objects.filter(auto__plate="CBA-1234").values(
            "id", "time", "paid", "left"
        )
        serializer = self.serializer(historic=results)
        list_historic = serializer.mount_payload()
        self.assertIsInstance(list_historic, list)

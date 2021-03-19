from rest_framework import serializers
from .interfaces import ISerializer


class CheckInSerializer(ISerializer):

    def __init__(self, parking):
        self.parking = parking
        self.create_message()

    def mount_payload(self):
        return {
            "msg": "Check-in created",
            "date": self.parking.time,
            "plate": self.parking.auto.plate
        }

    def create_message(self):
        return self.mount_payload()


class CheckOutSerializer(ISerializer):

    def __init__(self, parking):
        self.parking = parking
        self.create_message()

    def mount_payload(self):
        return {
            "msg": "Check-out done",
            "id": self.parking.id,
            "plate": self.parking.auto.plate
        }

    def create_message(self):
        return self.mount_payload()


class DoPaymentSerializer(ISerializer):

    def __init__(self, parking):
        self.parking = parking
        self.create_message()

    def mount_payload(self):
        return {
            "msg": "Payment done",
            "id": self.parking.id,
            "plate": self.parking.auto.plate
        }

    def create_message(self):
        return self.mount_payload()


class HistoricSerializer(ISerializer):

    def __init__(self, historic):
        self.historic = historic
        self.create_message()

    def mount_payload(self):
        list_historic: list = []
        for parking in self.historic:
            histo = {
                    "id": parking.id,
                    "time": parking.time,
                    "paid": parking.paid,
                    "left": parking.left
                    }
            list_historic.append(histo)
        return list_historic

    def create_message(self):
        return self.mount_payload()
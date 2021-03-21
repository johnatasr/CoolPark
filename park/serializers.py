from rest_framework import serializers
from .interfaces import ISerializer


class DefaultSerializer(ISerializer):

    def __init__(self, parking: object, msg: str):
        self.parking = parking
        self.msg = msg
        self.create_message()

    def mount_payload(self):
        return {
            "msg": self.msg,
            "date": self.parking.time,
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
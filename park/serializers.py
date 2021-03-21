from .interfaces import ISerializer


class DefaultSerializer(ISerializer):

    def __init__(self, parking: object, msg: str):
        self.parking = parking
        self.msg = msg

    def mount_payload(self):
        payload: dict = {
            "id": self.parking.id,
            "msg": self.msg,
            "plate": self.parking.auto.plate
        }
        return payload

    def create_message(self):
        message = self.mount_payload()
        return message


class HistoricSerializer(ISerializer):

    def __init__(self, historic):
        self.historic = historic
        self.create_message()

    def mount_payload(self):
        list_historic: list = []
        for parking in self.historic.iterator():
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
from configs.exceptions import InteratorException
from .interfaces import IIterator
from typing import Any

"""
      In Iterators occour all iteration beetween repositories, serializers and validators
      adding the business rules in process
"""


class CheckInIterator(IIterator):
    """ "
    Interactor responsible for check-in, called by API
    """

    def __init__(self, validator=None, repo=None, serializer=None):
        self.validator: object = validator
        self.repo: object = repo()
        self.serializer: object = serializer

    def set_params(self, park_payload: dict):
        self.payload = park_payload
        return self

    def execute(self):
        try:
            valided_payload = self.validator().validate_payload(self.payload)

            if valided_payload:
                plate: str = self.payload["plate"]
                created_parking_ocurrency = self.repo.create_parking_ocurrency_by_plate(
                    plate=plate
                )

                serialized_return = self.serializer(
                    parking=created_parking_ocurrency, msg="Check-in created"
                ).create_message()
                return serialized_return
        except InteratorException as error:
            raise InteratorException(error)


class CheckOutIterator(IIterator):
    """ "
    Interactor responsible for check-out, called by API
    """

    def __init__(self, validator=None, repo=None, serializer=None):
        self.validator: object = validator
        self.repo: object = repo()
        self.serializer: object = serializer

    def set_params(self, parking_id: Any):
        self.parking_id = parking_id
        return self

    def execute(self):
        try:
            if isinstance(self.parking_id, str):
                self.parking_id = int(self.parking_id)

            parking: object = self.repo.get_parking_ocurrency_by_id(id=self.parking_id)

            if parking.exists():
                parking: object = parking.first()
                if parking.paid:
                    if parking.left:
                        serialize = {"msg": "Check-out already done", "id": parking.id}
                        return serialize
                    parking_entity = self.repo.update_parking_ocurrency_checkout(
                        parking
                    )
                    serialize = self.serializer(
                        parking=parking_entity, msg="Check-out done"
                    ).create_message()
                    return serialize
                else:
                    serialize = {
                        "msg": "Cannot Check-out, payment not done",
                        "id": parking.id,
                    }
                    return serialize
            else:
                serialize = {"msg": f"Parking not found with ID : {self.parking_id}"}
                return serialize

        except InteratorException as error:
            raise InteratorException(error)


class DoPaymentIterator(IIterator):
    """
    Interactor responsible for the payment API process
    """

    def __init__(self, validator=None, repo=None, serializer=None):
        self.validator: object = validator
        self.repo: object = repo()
        self.serializer: object = serializer

    def set_params(self, parking_id: Any):
        self.parking_id = parking_id
        return self

    def execute(self):
        try:
            if isinstance(self.parking_id, str):
                self.parking_id = int(self.parking_id)

            parking = self.repo.get_parking_ocurrency_by_id(id=self.parking_id)

            if parking.exists():
                parking: object = parking.first()

                if parking.paid:
                    serialize = {"msg": "Payment already done", "id": parking.id}
                    return serialize

                parking_entity = self.repo.update_parking_ocurrency_pay(parking)
                serialize = self.serializer(
                    parking=parking_entity, msg="Payment done"
                ).create_message()
                return serialize
            else:
                serialize = {"msg": f"Parking not found with ID : {self.parking_id}"}
                return serialize

        except InteratorException as error:
            raise InteratorException(error)


class HistoricIterator(IIterator):
    """
    Interactor responsible for the history of parking by the registered license plate
    """

    def __init__(self, validator=None, repo=None, serializer=None):
        self.validator: object = validator
        self.repo: object = repo
        self.serializer: object = serializer

    def set_params(self, plate: str):
        self.plate = plate
        return self

    def execute(self):
        try:
            valided_plate = self.validator().validate_only_plate(self.plate)

            if valided_plate:
                historic = self.repo().get_historic_by_plate(self.plate)

                if historic.exists():
                    historic_cached = historic
                    serialize = self.serializer(historic_cached).create_message()
                    return serialize
                else:
                    serialize = {"msg": f"Historic not found with plate : {self.plate}"}
                    return serialize

        except InteratorException as error:
            raise InteratorException(error)

from .interfaces import IIterator
from coolpark.configs.exceptions import InteratorException
from typing import Any


class CheckInInterator(IIterator):
    """
        No interator ocorre a interação com grande parte dos modulos e libs
    """
    def __init__(self, validator=None, repo=None, serializer=None):
        """
            Inicializa a injecao de dependencia
        """
        self.validator: object = validator
        self.repo: object = repo
        self.serializer: object = serializer

    def set_params(self, park_payload: (dict, list)):
        """
            Configura os paramentros
        """
        self.payload = park_payload
        return self

    def execute(self):
        """
            Executa o fluxo a qual o interator foi designado
        """
        try:
            valided_payload = self.validator().validate_payload(self.payload, update=False)

            if valided_payload:
                created_parking_ocurrency = self.repo.create_parking_ocurrency(self.payload)
                serialized_return = self.serializer(created_parking_ocurrency)
                return serialized_return
        except InteratorException as error:
            raise InteratorException(error)


class CheckOutInterator(IIterator):
    """
        No interator ocorre a interação com grande parte dos modulos e libs
    """
    def __init__(self, validator=None, repo=None, serializer=None):
        """
            Inicializa a injecao de dependencia
        """
        self.validator: object = validator
        self.repo: object = repo
        self.serializer: object = serializer

    def set_params(self, parking_id: Any):
        """
            Configura os paramentros
        """
        self.parking_id = parking_id
        return self

    def execute(self):
        """
            Executa o fluxo a qual o interator foi designado
        """
        try:
            if isinstance(self.parking_id, str):
                self.parking_id = int(self.parking_id)

            parking = self.repo.get_parking_ocurrency_by_id(self.parking_id)

            if parking.exits():
                if parking.paid:
                    parking_entity = self.repo.update_parking_ocurrency_checkout(parking)
                    serialize = self.serializer(parking_entity)
                    return serialize
                else:
                    serialize = {"msg": "Cannot do Check-out, payment not done", "plate": parking.plate}
                    return serialize
            else:
                serialize = {"msg": f"Parking not found with ID : {self.parking_id}"}
                return serialize

        except InteratorException as error:
            raise InteratorException(error)


class DoPaymentInterator(IIterator):
    """
        No interator ocorre a interação com grande parte dos modulos e libs
    """
    def __init__(self, validator=None, repo=None, serializer=None):
        """
            Inicializa a injecao de dependencia
        """
        self.validator: object = validator
        self.repo: object = repo
        self.serializer: object = serializer

    def set_params(self, parking_id: Any):
        """
            Configura os paramentros
        """
        self.parking_id = parking_id
        return self

    def execute(self):
        """
            Executa o fluxo a qual o interator foi designado
        """
        try:
            if isinstance(self.parking_id, str):
                self.parking_id = int(self.parking_id)

            parking = self.repo.get_parking_ocurrency_by_id(self.parking_id)

            if parking.exits():
                parking_entity = self.repo.update_parking_ocurrency_pay(parking)
                serialize = self.serializer(parking_entity)
                return serialize
            else:
                serialize = {"msg": f"Parking not found with ID : {self.parking_id}"}
                return serialize

        except InteratorException as error:
            raise InteratorException(error)


class HistoricInterator(IIterator):
    """
        No interator ocorre a interação com grande parte dos modulos e libs
    """
    def __init__(self, validator=None, repo=None, serializer=None):
        """
            Inicializa a injecao de dependencia
        """
        self.validator: object = validator
        self.repo: object = repo
        self.serializer: object = serializer

    def set_params(self, plate: str):
        """
            Configura os paramentros
        """
        self.plate = plate
        return self

    def execute(self):
        """
            Executa o fluxo a qual o interator foi designado
        """
        try:
            valided_plate = self.validator().validate_only_plate(self.plate)

            if valided_plate:
                historic = self.repo.get_historic_parking_ocurrency_by_plate(self.plate)

                if historic.exits():
                    serialize = self.serializer(historic)
                    return serialize
                else:
                    serialize = {"msg": f"Parking not found with plate : {self.plate}"}
                    return serialize

        except InteratorException as error:
            raise InteratorException(error)
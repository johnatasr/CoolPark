from .repository import ParkRepo
from .interators import (
    CheckInInterator,
    CheckOutInterator,
    DoPaymentInterator,
    HistoricInterator
)
from .validators import ParkValidator
from .serializers import (
    DefaultSerializer,
    HistoricSerializer
)
from typing import Any


class ParkFactory:

    @staticmethod
    def create_check_in_interator(data: dict):
        return CheckInInterator(validator=ParkValidator,
                                repo=ParkRepo,
                                serializer=DefaultSerializer).set_params(park_payload=data).execute()

    @staticmethod
    def create_check_out_interator(id: Any):
        return CheckOutInterator(repo=ParkRepo, serializar=DefaultSerializer)\
                                            .set_params(parking_id=id).execute()

    @staticmethod
    def create_do_payment_interator(id: Any):
        return DoPaymentInterator(repo=ParkRepo, serializar=DefaultSerializer)\
                                            .set_params(parking_id=id).execute()

    @staticmethod
    def create_historic_interator(plate: str):
        return HistoricInterator(repo=ParkRepo, serializar=HistoricSerializer)\
                                            .set_params(plate=plate).execute()


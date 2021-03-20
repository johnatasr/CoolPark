from coolpark.automobilies.repositories import AutomobiliesRepo
from .repository import ParkRepo
from .interators import (
    CheckInInterator,
    CheckOutInterator,
    DoPaymentInterator,
    HistoricInterator
)
from .validators import ParkValidator
from .serializers import (
    CheckInSerializer,
    CheckOutSerializer,
    DoPaymentSerializer,
    HistoricSerializer
)
from typing import Any


class ParkFactory:

    @staticmethod
    def create_check_in_interator(data: dict):
        return CheckInInterator(validator=ParkValidator,
                                repo=ParkRepo,
                                serializar=CheckInSerializer).set_params(park_payload=data).execute()

    @staticmethod
    def create_check_out_interator(id: Any):
        return CheckOutInterator(repo=ParkRepo, serializar=CheckOutSerializer)\
                                            .set_params(parking_id=id).execute()

    @staticmethod
    def do_payment_interator(id: Any):
        return DoPaymentInterator(repo=ParkRepo, serializar=DoPaymentSerializer)\
                                            .set_params(parking_id=id).execute()

    @staticmethod
    def historic_interator(plate: str):
        return HistoricInterator(repo=ParkRepo, serializar=HistoricSerializer)\
                                            .set_params(plate=plate).execute()

    @staticmethod
    def create_new_auto(auto_payload: dict):
        return AutomobiliesRepo().create_auto(auto_payload)

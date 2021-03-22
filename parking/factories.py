from .repository import ParkRepo
from .iterators import (
    CheckInIterator,
    CheckOutIterator,
    DoPaymentIterator,
    HistoricIterator,
)
from .validators import ParkValidator
from .serializers import DefaultSerializer, HistoricSerializer
from typing import Any


class ParkFactory:
    @staticmethod
    def create_check_in_interator(data: dict):
        return (
            CheckInIterator(
                validator=ParkValidator, repo=ParkRepo, serializer=DefaultSerializer
            )
            .set_params(park_payload=data)
            .execute()
        )

    @staticmethod
    def create_check_out_interator(id: Any):
        return (
            CheckOutIterator(repo=ParkRepo, serializer=DefaultSerializer)
            .set_params(parking_id=id)
            .execute()
        )

    @staticmethod
    def create_do_payment_interator(id: Any):
        return (
            DoPaymentIterator(repo=ParkRepo, serializer=DefaultSerializer)
            .set_params(parking_id=id)
            .execute()
        )

    @staticmethod
    def create_historic_interator(plate: str):
        return (
            HistoricIterator(
                validator=ParkValidator, repo=ParkRepo, serializer=HistoricSerializer
            )
            .set_params(plate=plate)
            .execute()
        )

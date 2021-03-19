from coolpark.configs.exceptions import ConflictException
from .helpers import ParkingHelpers
from .factories import ParkFactory
from .entities import (
    Park as ParkEntity,
    ParkingOcurrency as ParkingOcurrencyEntity,
)
from .models import (
    ParkingOcurrency,
    Park
)

from typing import Any


class ParkRepo:
    """
        Camada onde ocorre a interação do Interator com as Entidades e Modelos,
        Ocorre tambem grande parte da regra de negocio
    """

    helper = ParkingHelpers()
    factory = ParkFactory()

    def get_or_create_park_model(self):
        """
            Cria uma lista de Entidade Skills no formato final
        """
        try:
            return Park().load()
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Não possível skill, erro : {err}')

    def create_parking_ocurrency_model(self, parking_object: object):
        """
            Cria a Entidade final para serializacao
        """
        try:
            return ParkingOcurrency(
                time=parking_object.time,
                paid=parking_object.paid,
                left=parking_object.left,
                auto=parking_object.auto
            ).save()
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                          message=f'Não possível criar busca, erro : {err}')

    def create_park_entity(self, park: Any):
        """
            Cria a Entidade base Freelance
        """
        try:
            if isinstance(park, object):
                return ParkEntity(
                    id=park.id,
                    park_ocurrencies=park.parking_ocurrencies,
                )
            if isinstance(park, (dict, list)):
                return ParkEntity(
                    id=park['id'],
                    park_ocurrencies=park['parking_ocurrencies'],
                )
            raise ConflictException

        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                          message=f'Não possível criar busca, erro : {err}')


    def create_parking_ocurrency_entity(self, parking_ocurrency: Any):
        """
            Cria a Entidade base Freelance
        """
        try:
            if isinstance(parking_ocurrency, object):
                return ParkingOcurrencyEntity(
                    id=parking_ocurrency.id,
                    time=parking_ocurrency.time,
                    paid=parking_ocurrency.paid,
                    left=parking_ocurrency.left,
                    auto=parking_ocurrency.auto
                )
            if isinstance(parking_ocurrency, (dict, list)):
                return ParkingOcurrencyEntity(
                    id=parking_ocurrency['id'],
                    time=parking_ocurrency['time'],
                    paid=parking_ocurrency['paid'],
                    left=parking_ocurrency['left'],
                    auto=parking_ocurrency['auto']
                )
            raise ConflictException

        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Error in create a ocurreny_entity from model : {err}')

    def create_parking_ocurrency(self, payload):
        try:
            park = self.get_or_create_park_model()
            parking_ocurrency_entity = self.create_parking_ocurrency_entity(
                {
                    "time": self.helper.get_today(),
                    "paid": False,
                    "left": False,
                    "auto": self.factory.create_new_auto(payload)
                })

            parking_ocurrency = self.create_parking_ocurrency_model(parking_ocurrency_entity)
            park.parking_ocurrencies.add(parking_ocurrency)
            park.save()

            return parking_ocurrency_entity
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Error in create a ocurreny : {err}')

    def get_parking_ocurrency_by_id(self, id: int):
        return ParkingOcurrency.objects.filter(id=id)

    def get_historic_parking_ocurrency_by_plate(self, plate: str):
        return ParkingOcurrency.objects.filter(auto__plate=plate)

    def update_parking_ocurrency_checkout(self, parking: object):
        try:
            exit_datetime = self.helper.get_today()
            formated_exit_date = self.helper.transform_date_checkout(
                                                start_date=parking.time,
                                                end_date=exit_datetime)

            parking.update(left=True, time=formated_exit_date)
            parking.save()

            return self.create_parking_ocurrency_entity(parking)
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Error in update checkout a ocurreny : {err}')

    def update_parking_ocurrency_pay(self, parking: object):
        try:
            parking.update(paid=True)
            parking.save()

            return self.create_parking_ocurrency_entity(parking)
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Error in update pay a ocurreny : {err}')





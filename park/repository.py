from configs.exceptions import ConflictException
from automobilies.repositories import AutomobiliesRepo
from .helpers import ParkingHelpers
from .entities import (
    ParkingOcurrency as ParkingOcurrencyEntity,
)
from .models import (
    ParkingOcurrency,
    Park
)

from typing import Any, Type


class ParkRepo:
    """
        Camada onde ocorre a interação do Interator com as Entidades e Modelos,
        Ocorre tambem grande parte da regra de negocio
    """

    helper: Type[ParkingHelpers] = ParkingHelpers()

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
            parking_created_model = ParkingOcurrency(
                        paid=parking_object.paid,
                        left=parking_object.left,
                        auto=parking_object.auto
                        )
            parking_created_model.save()
            return parking_created_model
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                          message=f'Não possível criar busca, erro : {err}')

    def create_parking_ocurrency_entity(self, parking_ocurrency: Any, type_object=False):
        """
            Cria a Entidade base Freelance
        """
        try:
            return ParkingOcurrencyEntity(
                paid=parking_ocurrency.paid if type_object else parking_ocurrency['paid'],
                left=parking_ocurrency.left if type_object else parking_ocurrency['left'],
                auto=parking_ocurrency.auto if type_object else parking_ocurrency['auto'])

        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Error in create a ocurreny_entity from model : {err}')

    def create_parking_ocurrency_by_plate(self, plate: str) -> Type[ParkingOcurrencyEntity]:
        try:
            park: Type[Park] = self.get_or_create_park_model()
            automobilie = AutomobiliesRepo().create_auto(plate)
            parking_ocurrency_entity: Type[ParkingOcurrencyEntity] = self.create_parking_ocurrency_entity(
                {
                    "paid": False,
                    "left": False,
                    "auto": automobilie
                }, type_object=False)

            parking_ocurrency = self.create_parking_ocurrency_model(parking_ocurrency_entity)
            parking_ocurrency_entity.set_id(parking_ocurrency.id)
            park.parking_ocurrencies.add(parking_ocurrency)
            park.save()

            return parking_ocurrency_entity
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Error in create a ocurreny : {err}')

    def get_parking_ocurrency_by_id(self, id: int):
        return ParkingOcurrency.objects.filter(id=id)

    def get_historic_by_plate(self, plate: str):
        return ParkingOcurrency.objects.filter(auto__plate=plate)

    def update_parking_ocurrency_checkout(self, parking: object):
        try:
            exit_datetime = self.helper.get_today()
            formated_exit_date = self.helper.transform_date_checkout(
                start_date=parking.entry,
                end_date=exit_datetime)

            parking.left = True
            parking.exit = exit_datetime
            parking.time = formated_exit_date
            parking.save()

            parking_entity = self.create_parking_ocurrency_entity(parking, type_object=True)
            parking_entity.set_id(parking.id)

            return parking_entity
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Error in update checkout a ocurreny : {err}')

    def update_parking_ocurrency_pay(self, parking: object):
        try:
            parking.paid = True
            parking.save()
            parking_entity = self.create_parking_ocurrency_entity(parking, type_object=True)
            parking_entity.set_id(parking.id)
            return parking_entity
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Error in update pay a ocurreny : {err}')





from configs.exceptions import ConflictException
from automobilies.repositories import AutomobiliesRepo
from .helpers import ParkingHelpers
from .entities import (
    ParkingOcurrency as ParkingOcurrencyEntity,
)
from .models import ParkingOcurrency, Parking

from typing import Any, Type


class ParkRepo:
    """
    This layer is responsible for interacting with models and entities
    """

    helper: Type[ParkingHelpers] = ParkingHelpers()

    def get_or_create_parking_base_model(self) -> Type[Parking]:
        """
        Create a Parking model
        """
        try:
            return Parking().load()
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_create",
                message=f"Error in load Park objects: {err}",
            )

    def create_parking_ocurrency_model(
        self, parking_object: object
    ) -> Type[ParkingOcurrency]:
        """
        Create a Parking Ocurrenvy model
        """
        try:
            parking_created_model = ParkingOcurrency(
                paid=parking_object.paid,
                left=parking_object.left,
                auto=parking_object.auto,
            )
            parking_created_model.save()
            return parking_created_model
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_create",
                message=f"Error in create a ocurreny_model: {err}",
            )

    def create_parking_ocurrency_entity(
        self, parking_ocurrency: Any, type_object=False
    ) -> Type[ParkingOcurrencyEntity]:
        """
        Create a Parking Ocurrenvy object Entity
        """
        try:
            return ParkingOcurrencyEntity(
                paid=parking_ocurrency.paid
                if type_object
                else parking_ocurrency["paid"],
                left=parking_ocurrency.left
                if type_object
                else parking_ocurrency["left"],
                auto=parking_ocurrency.auto
                if type_object
                else parking_ocurrency["auto"],
            )

        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_create",
                message=f"Error in create a ocurreny_entity: {err}",
            )

    def create_parking_ocurrency_by_plate(
        self, plate: str
    ) -> Type[ParkingOcurrencyEntity]:
        """
        Create a parking ocurrency by plate, this is the main method called by Check-in Api
        to create a new parking instance
        """
        try:
            park: Type[Parking] = self.get_or_create_parking_base_model()
            automobilie = AutomobiliesRepo().create_auto(plate)
            parking_ocurrency_entity: Type[
                ParkingOcurrencyEntity
            ] = self.create_parking_ocurrency_entity(
                {"paid": False, "left": False, "auto": automobilie}, type_object=False
            )

            parking_ocurrency = self.create_parking_ocurrency_model(
                parking_ocurrency_entity
            )
            park.parking_ocurrencies.add(parking_ocurrency)
            park.save()

            parking_ocurrency_entity.set_id(parking_ocurrency.id)

            return parking_ocurrency_entity
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_create",
                message=f"Error in create a parking by plate : {err}",
            )

    def get_parking_ocurrency_by_id(self, id: int) -> Type[ParkingOcurrency]:
        """ "
        Search a parking by Parking Ocurrency model id
        """
        return ParkingOcurrency.objects.filter(id=id)

    def get_historic_by_plate(self, plate: str) -> Type[ParkingOcurrency]:
        """ "
        Search a parking by Automobilie model plate
        """
        return ParkingOcurrency.objects.filter(auto__plate=plate).values(
            "id", "time", "paid", "left", "auto"
        )

    def update_parking_ocurrency_checkout(
        self, parking: object
    ) -> Type[ParkingOcurrencyEntity]:
        """ "
        Update the parking ocurrency called by Check-out iterator
        """
        try:
            exit_datetime = self.helper.get_today()
            formated_exit_date = self.helper.transform_date_checkout(
                start_date=parking.entry, end_date=exit_datetime
            )

            parking.left = True
            parking.exit = exit_datetime
            parking.time = formated_exit_date
            parking.save()

            parking_entity = self.create_parking_ocurrency_entity(
                parking, type_object=True
            )
            parking_entity.set_id(parking.id)

            return parking_entity
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_update",
                message=f"Error in update checkout a ocurreny : {err}",
            )

    def update_parking_ocurrency_pay(
        self, parking: object
    ) -> Type[ParkingOcurrencyEntity]:
        """ "
        Update the parking ocurrency called by Do-Payment iterator
        """
        try:
            parking.paid = True
            parking.save()
            parking_entity = self.create_parking_ocurrency_entity(
                parking, type_object=True
            )
            parking_entity.set_id(parking.id)
            return parking_entity
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_update",
                message=f"Error in update pay a ocurreny : {err}",
            )

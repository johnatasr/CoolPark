from configs.exceptions import ConflictException
from .entities import Automobilie
from .models import Automobilie as AutomobilieModel

from typing import Any


class AutomobiliesRepo:
    def create_auto_model(self, auto_entity):
        """
        Save the model Automobilie with the Entity created previously
        """
        automobilie = AutomobilieModel.objects.create(plate=auto_entity.plate)
        automobilie.save()
        return automobilie

    def create_auto(self, plate: str):
        """
        Create a Entity Automobilie saving in database the model object
        """
        try:
            entity = Automobilie(plate=plate)
            automobilie = self.create_auto_model(entity)

            return automobilie
        except ConflictException as err:
            raise ConflictException(
                source="repository",
                code="conflit_in_create",
                message=f"Não possível skill, erro : {err}",
            )

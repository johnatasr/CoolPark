from configs.exceptions import ConflictException
from .entities import Automobilie
from .models import Automobilie as AutomobilieModel

from typing import Any


class AutomobiliesRepo:
    """
        Camada onde ocorre a interação do Interator com as Entidades e Modelos,
        Ocorre tambem grande parte da regra de negocio
    """

    def create_auto_model(self, auto_entity):
        automobilie = AutomobilieModel.objects.create(plate=auto_entity.plate)
        automobilie.save()
        return automobilie

    def create_auto(self, plate: str):
        """
            Cria uma lista de Entidade Skills no formato final
        """
        try:
            entity = Automobilie(plate=plate)
            automobilie = self.create_auto_model(entity)

            return automobilie
        except ConflictException as err:
            raise ConflictException(source='repository', code='conflit_in_create',
                                    message=f'Não possível skill, erro : {err}')


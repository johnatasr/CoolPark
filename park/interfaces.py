from typing import Type, List, Any
from abc import ABC, abstractmethod


class IValidator(ABC):
    """ Interface para o Validator"""

    @abstractmethod
    def validate(self, value: bool) -> bool:
        raise Exception("Validator deve implementar o método: valid")

    @abstractmethod
    def is_empty_payload(self) -> bool:
        raise Exception("Validator deve implementar o método: is_empty_payload")

    @abstractmethod
    def validate_payload(self) -> (bool, dict):
        raise Exception("Validator deve implementar o método: validate_payload")


class IIterator(ABC):
    """ Interface para o Interator """

    @abstractmethod
    def set_params(self, *args, **kwargs):
        raise Exception("Interator deve implementar o método: set_params")

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        raise Exception("Interator deve implementar o método: execute")


class ISerializer(ABC):
    """ Interface para o Serializer """

    @abstractmethod
    def create_message(self) -> dict:
        raise Exception("Serializer deve implementar o método: serialize_object")

    @abstractmethod
    def mount_payload(self, payload: dict) -> dict:
        raise Exception("Serializer deve implementar o método: mount_payload")
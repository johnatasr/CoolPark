from configs.exceptions import InvalidPayloadException
from .interfaces import IValidator
from .helpers import ParkingHelpers


class ParkValidator(IValidator):

    DEFAULT_PLATE_MASK: str = "[A-Z]{3}-[0-9]{4}\Z"

    def __init__(self):
        self.helper = ParkingHelpers()

    @staticmethod
    def validate(value: bool) -> bool:
        return value

    def is_empty_payload(self, payload) -> (bool, Exception):
        if isinstance(payload, (dict, object, list, bytes)):
            return True
        else:
            raise InvalidPayloadException(
                source="validator",
                code="empty_payload",
                message="Payload in request is empty",
            )

    def validate_only_plate(self, plate: str) -> (bool, Exception):
        return self.helper.regex_validate(plate, self.DEFAULT_PLATE_MASK)

    def validate_payload(self, payload) -> list:
        self.is_empty_payload(payload)

        if "plate" not in payload:
            raise InvalidPayloadException(
                source="validator",
                code="field_not_exists",
                message="Field required: plate",
            )
        if len(payload["plate"]) < 8:
            raise InvalidPayloadException(
                source="validator",
                code="field_size_not_allowed",
                message="Field plate don't should be less than 8",
            )
        if len(payload["plate"]) > 8:
            raise InvalidPayloadException(
                source="validator",
                code="field_size_not_allowed",
                message="Field plate don't should be major than 8",
            )

        if not self.validate_only_plate(payload["plate"]):
            raise InvalidPayloadException(
                source="validator",
                code="field_not_allowed",
                message="Wrong format plate. Field should be in this format AAA-9999",
            )

        return self.validate(True)

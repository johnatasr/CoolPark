from typing import Type
from django.utils import timezone
from dateutil import relativedelta
from datetime import datetime
import re


class ParkingHelpers:
    @staticmethod
    def transform_date_checkout(
        start_date: Type[datetime], end_date: Type[datetime]
    ) -> str:
        """ "
        Transform the range of dates in a string representation
        """
        result = relativedelta.relativedelta(end_date, start_date)
        msg: str = ""

        if result.hours >= 1:
            hours = "hours"
            if result.hours == 1:
                hours = "hour"
            msg += f"{result.hours} {hours}, "

        if result.minutes > 1:
            minutes = "minutes"
        else:
            minutes = "minute"

        msg += f"{result.minutes} {minutes}"

        return msg

    @staticmethod
    def regex_validate(plate: str, default_mask: str) -> bool:
        """ "
        Valid the plate using Regex
        """
        regex = re.compile(default_mask)
        valid = regex.match(plate)
        if valid:
            return True
        else:
            raise Exception("Plate don't match with default plate validation")

    @staticmethod
    def get_today() -> datetime:
        """ "
        Get the time of current system
        """
        return timezone.now()

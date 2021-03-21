from typing import Type
from django.utils import timezone
from dateutil import relativedelta
from datetime import datetime
import re


class ParkingHelpers:

    @staticmethod
    def transform_date_checkout(start_date: Type[datetime], end_date: Type[datetime]):
        result = relativedelta.relativedelta(end_date, start_date)
        msg: str = ''

        if result.hours >= 1:
            hours = 'hours'
            if result.hours == 1:
                hours = 'hour'
            msg += f"{result.hours} {hours}, "

        if result.minutes > 1:
            minutes = 'minutes'
        else:
            minutes = 'minute'

        msg += f"{result.minutes} {minutes}"

        return msg

    @staticmethod
    def regex_validate(plate: str, default_mask: str) -> bool:
        regex = re.compile(default_mask)
        valid = regex.match(plate)
        if valid:
            return True
        else:
            raise Exception("Plate don't match with default plate validation")


    @staticmethod
    def get_today():
        return timezone.now()

    @staticmethod
    def payload_time_message(date: Type[datetime]):
        return date.strftime('%d/%m/%Y - %H:%M')


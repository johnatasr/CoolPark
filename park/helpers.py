from typing import Type
from datetime import datetime
from dateutil import relativedelta
import re


class ParkingHelpers:

    @staticmethod
    def transform_date_checkout(start_date: Type[datetime], end_date: Type[datetime]):
        result = relativedelta.relativedelta(end_date, start_date)
        return result

    @staticmethod
    def regex_validate(plate: str, default_mask: str) -> bool:
        try:
            regex = re.compile(default_mask)
            regex.match(plate)
            return True
        except Exception:
            raise Exception("Plate don't match with default plate validation")

    @staticmethod
    def get_today():
        return datetime.today()


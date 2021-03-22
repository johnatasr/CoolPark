from typing import List, Type
from datetime import datetime
from automobilies.models import Automobilie


class ParkingOcurrency:
    """
    Representation in Object of Model ParkingOcurrency
    """

    def __init__(self, paid: bool, left: bool, auto: Type[Automobilie]):

        self._id = None
        self._time = None
        self._entry = None
        self._exit = None
        self._paid = paid
        self._left = left
        self._auto = auto

    def __repr__(self):
        return f"Entity: ParkingOcurrency<id:{self.id}, time:{self.time}, paid:{self.paid}, left:{self.left}, auto:{self.auto.plate}>"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(("id", self.id, "time", self.time))

    @property
    def id(self):
        return self._id

    def set_id(self, id: int):
        self._id = id

    @property
    def time(self):
        return self._time

    def set_time(self, time_string: str):
        self._time = time_string

    @property
    def entry(self):
        return self._entry

    def set_entry(self, entry: Type[datetime]):
        self._entry = entry

    @property
    def exit(self):
        return self._exit

    def set_exit(self, exit: Type[datetime]):
        self._exit = exit

    @property
    def paid(self):
        return self._paid

    @property
    def left(self):
        return self._left

    @property
    def auto(self):
        return self._auto

    @property
    def auto_plate(self):
        return self._auto.plate


class Parking:
    """
    Representation in Object of Model Parking
    """

    def __init__(self, park_ocurrencies: List[ParkingOcurrency]):
        self._id = None
        self._park_ocurrencies = park_ocurrencies

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    @property
    def id(self):
        return self._id

    def set_id(self, id: int):
        self._id = id

    @property
    def park_ocurrencies(self):
        return self.park_ocurrencies

from typing import List, Type
from datetime import datetime
from automobilies.models import Automobilie


class ParkingOcurrency:

    def __init__(self,
                 id: int,
                 time: Type[datetime],
                 paid: bool,
                 left: bool,
                 auto: Type[Automobilie]):

        self._id = id
        self._time = time
        self._paid = paid
        self._left = left
        self._auto = auto

    def __repr__(self):
        return f"Entity: ParkingOcurrency<id:{self.id}, time:{self.time},  \
               paid:{self.paid}, left:{self.left}, auto:{self.auto.plate}>"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(("id", self.id, "time", self.time))

    @property
    def id(self):
        return self._id

    @property
    def time(self):
        return self._time

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


class Park:

    def __init__(self, id: int , park_ocurrencies: List[ParkingOcurrency]):
        self._id = id
        self._park_ocurrencies = park_ocurrencies

    def __repr__(self):
        return f"Entity: Park<id:{self.id}, park_ocurrencies:{self.park_ocurrencies}>"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(("id", self.id, "name", self.name))

    @property
    def id(self):
        return self._id

    @property
    def park_ocurrencies(self):
        return self.park_ocurrencies




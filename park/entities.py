from pydantic import BaseModel
from typing import List, Type
from datetime import datetime
from coolpark.automobilies.models import Automobilie


class ParkingOcurrency(BaseModel):
    _id: int
    _time: Type[datetime]
    _paid: bool
    _left: bool
    _auto: Type[Automobilie]

    def __repr__(self):
        return f"Entity: ParkingOcurrency<id:{self.id}, time:{self.time},  \
               paid:{self.paid}, left:{self.left}, auto:{self.auto.plate}>"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

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


class Park(BaseModel):
    _id: int
    _park_ocurrencies: List[ParkingOcurrency]

    def __repr__(self):
        return f"Entity: Park<id:{self.id}, park_ocurrencies:{self.park_ocurrencies}>"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    @property
    def id(self):
        return self._id

    @property
    def park_ocurrencies(self):
        return self.park_ocurrencies




from pydantic import BaseModel


class Automobilie(BaseModel):
    _id: int
    _plate: str

    def __repr__(self):
        return f"Entity: Automobilie<id:{self.id},  plate:{self.plate}>"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

    @property
    def id(self):
        return self._id

    @property
    def plate(self):
        return self._plate
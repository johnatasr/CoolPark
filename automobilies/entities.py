class Automobilie:
    def __init__(self, plate: str):
        self._id = None
        self._plate = plate

    def __repr__(self):
        return f"Entity: Automobilie<id:{self.id},  plate:{self.plate}>"

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
    def plate(self):
        return self._plate

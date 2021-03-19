from pydantic import BaseModel
from typing import List, Type
from datetime import datetime
# from .helpers import


class Automobilie(BaseModel):
    id: int
    plate: str

    def __repr__(self):
        return f"Entity: Automobilie<id:{self.id},  plate:{self.plate}>"

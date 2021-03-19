from pydantic import BaseModel
from typing import List, Type
from datetime import datetime
# from .helpers import


class ParkingOcurrency(BaseModel):
    id: int
    time: Type[datetime]
    paid: bool
    left: bool
    auto: Type[Automobilie]

    def __repr__(self):
        return f"Entity: ParkingOcurrency<id:{self.id}, time:{self.time},  \
               paid:{self.paid}, left:{self.left}, auto:{self.auto.plate}>"

    # @property
    # def full_name(self) -> str:
    #     return self.user.full_name
    #
    # @property
    # def skills(self) -> List:
    #     skills = []
    #     for professional_experience in self.professionalExperiences:
    #         skills += professional_experience.skills
    #     return list(set(skills))
    #
    # @property
    # def get_formated_date(self) -> Type[datetime]:

    #
    #
    #
    #     return result
    #
    # def get_duration_in_months_by_skill(self) -> Dict[str, int]:
    #     skills = {}
    #     for skill, date_ranges in self.get_date_ranges_by_skill().items():
    #         all_days_experience = get_all_days_experience(date_ranges)
    #         days = remove_overlapped_days(all_days_experience)
    #         num_days = get_num_days(days)
    #         num_months = get_num_months(num_days)
    #         skills[skill] = num_months
    #     return skills
    # def computed_skills(self):
    #     duration_in_months_by_skill = self.get_duration_in_months_by_skill()
    #     return [
    #         {
    #             "id": skill.id,
    #             "name": skill.name,
    #             "durationInMonths": duration_in_months_by_skill.get(skill.name),
    #         }
    #         for skill in self.skills
    #     ]



class Park(BaseModel):
    id: int
    park_ocurrencies: List[ParkingOcurrency]



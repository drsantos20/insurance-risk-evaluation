from enum import Enum

from pydantic import BaseModel


class ScoreEnum(str, Enum):
    economic = "economic"
    regular = "regular"
    responsible = "responsible"
    ineligible = "ineligible"


class InsuranceDTO(BaseModel):
    auto: ScoreEnum
    disability: ScoreEnum
    home: ScoreEnum
    life: ScoreEnum

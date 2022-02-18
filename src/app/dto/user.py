from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional, List
from typing_extensions import TypedDict


class MaritalStatus(str, Enum):
    married = "married"
    single = "single"


class OwnershipStatus(str, Enum):
    owned = "owned"
    mortgaged = "mortgaged"


class HouseDTO(TypedDict):
    ownership_status: OwnershipStatus


class VehicleData(int):
    year: int = Field(..., ge=0, description="Must be a valid year")


class VehicleDTO(TypedDict):
    year: VehicleData


class UserInformationDTO(BaseModel):
    age: int = Field(..., ge=0, description="Age must be greater than or equal to 0")

    dependents: int = Field(
        ..., ge=0, description="Dependents must be greater than or equal to 0"
    )

    income: int = Field(
        ..., ge=0, description="Income must be greater than or equal to 0"
    )

    marital_status: MaritalStatus

    risk_questions: List[bool] = Field(
        ...,
        min_items=3,
        max_items=3,
        description="Risk questions must have at least 3 itens",
    )

    house: Optional[HouseDTO]
    
    vehicle: Optional[VehicleDTO]

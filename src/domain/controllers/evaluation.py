from fastapi import APIRouter

from domain.dtos.user_profile import UserProfileDTO
from domain.dtos.insurance import InsuranceDTO
from domain.services import insurance_score

router = APIRouter(prefix="/insurance", tags=["insurance"])


@router.post("/evaluation", response_model=InsuranceDTO)
async def evaluation_risk(user_information: UserProfileDTO):
    return insurance_score.get_insurance_score(user_information)

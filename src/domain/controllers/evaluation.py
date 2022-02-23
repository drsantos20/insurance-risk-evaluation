from domain.dtos.insurance import InsuranceDTO
from domain.dtos.user_profile import UserProfileDTO
from domain.services import insurance_score
from fastapi import APIRouter

router = APIRouter(prefix="/insurance", tags=["insurance"])


@router.post("/evaluation", response_model=InsuranceDTO)
async def evaluation_risk(user_profilermation: UserProfileDTO):
    return insurance_score.get_insurance_score(user_profilermation)

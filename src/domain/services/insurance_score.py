from domain.dtos.insurance import InsuranceDTO
from domain.dtos.user_profile import UserProfileDTO
from domain.risk.category.age import (
    AgeBetweenThirtyAndForty,
    AgeOverSixty,
    AgeUnderThirty,
)
from domain.risk.category.dependents import HasDependents
from domain.risk.category.house import HasMotgagedHouse, HasNoHouse
from domain.risk.category.income import HasNoIncome, IncomeEvaluation
from domain.risk.category.marital import IsMaried
from domain.risk.category.vehicle import HasNoVehicle, HasVehicle
from domain.risk.user_profile_risk import UserProfileRisk


def get_insurance_score(user_profile: UserProfileDTO) -> InsuranceDTO:
    """
    Set insurance rules using | pipe operator
    """
    base_risk = UserProfileRisk(user_profile)
    rules = (
        AgeOverSixty()
        | AgeUnderThirty
        | AgeBetweenThirtyAndForty
        | HasDependents
        | HasMotgagedHouse
        | HasNoHouse
        | HasNoIncome
        | IncomeEvaluation
        | IsMaried
        | HasNoVehicle
        | HasVehicle
    )
    risk = rules.apply_rule(user_profile, base_risk)
    return risk.evaluate_risk_category()

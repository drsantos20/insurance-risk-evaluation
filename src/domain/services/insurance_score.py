from domain.dtos.insurance import InsuranceDTO
from domain.dtos.user_profile import UserProfileDTO
from domain.risk.categories.age import (
    AgeBetweenThirtyAndForty,
    AgeOverSixty,
    AgeUnderThirty,
)
from domain.risk.categories.dependents import HasDependents
from domain.risk.categories.house import HasMotgagedHouse, HasNoHouse
from domain.risk.categories.income import HasNoIncome, IncomeEvaluation
from domain.risk.categories.marital import IsMaried
from domain.risk.categories.vehicle import HasNoVehicle, HasVehicle
from domain.risk.user_risk import UserRisk


def get_insurance_score(user_info: UserProfileDTO) -> InsuranceDTO:
    """
    Set insurance rules using | pipe operator
    """
    base_risk = UserRisk(user_info)
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
    risk = rules.apply_rule(user_info, base_risk)
    return risk.evaluate_risk_category()

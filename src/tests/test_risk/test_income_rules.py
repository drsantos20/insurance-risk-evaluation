from domain.dtos.user_profile import UserProfileDTO
from domain.risk.categories.income import HasNoIncome, IncomeEvaluation
from domain.risk.user_risk import UserRisk


def test_has_no_income():
    user_info = {
        "age": 62,
        "dependents": 2,
        "income": 0,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserProfileDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    rule = HasNoIncome() | IncomeEvaluation
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User should not be eligible to disability
    assert risk.disability.is_eligible == False
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2


def test_income_above_two_hundred():
    user_info = {
        "age": 62,
        "dependents": 0,
        "income": 220000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserProfileDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    rule = HasNoIncome() | IncomeEvaluation
    risk = rule.apply_rule(user_dto, user_base_risk)
    # All risk lines should be reduced by 1
    assert risk.disability.risk == 1
    assert risk.auto.risk == 1
    assert risk.home.risk == 1
    assert risk.life.risk == 1


def test_no_rule():
    # No rule to apply
    user_info = {
        "age": 62,
        "dependents": 0,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserProfileDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    rule = HasNoIncome() | IncomeEvaluation
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User risk should not change
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2

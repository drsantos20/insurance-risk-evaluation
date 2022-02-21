from domain.dtos.user_profile import UserProfileDTO
from domain.risk.categories.dependents import HasDependents
from domain.risk.user_risk import UserRisk


def test_has_dependents():
    user_info = {
        "age": 62,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserProfileDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    rule = HasDependents()
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User should have 1 score point added to life and disability
    assert risk.disability.risk == 3
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 3


def test_no_dependents():
    user_info = {
        "age": 62,
        "dependents": 0,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserProfileDTO(**user_info)
    user_base_risk = UserRisk(user_dto)
    rule = HasDependents()
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User risk should not change
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2

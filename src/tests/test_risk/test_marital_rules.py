from domain.dtos.user_profile import UserProfileDTO
from domain.risk.user_profile_risk import UserProfileRisk
from domain.risk.category.marital import IsMaried


def test_is_maried():
    user_profile = {
        "age": 62,
        "dependents": 2,
        "income": 0,
        "marital_status": "married",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserProfileDTO(**user_profile)
    user_base_risk = UserProfileRisk(user_dto)
    rule = IsMaried()
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User should not be eligible to disability
    assert risk.disability.risk == 1
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 3


def test_is_single():
    user_profile = {
        "age": 62,
        "dependents": 0,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserProfileDTO(**user_profile)
    user_base_risk = UserProfileRisk(user_dto)
    rule = IsMaried()
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User risk should not change
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2

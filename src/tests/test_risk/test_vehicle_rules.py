from domain.dtos.user_profile import UserProfileDTO
from domain.risk.category.vehicle import HasNoVehicle, HasVehicle
from domain.risk.user_profile_risk import UserProfileRisk


def test_has_no_vehicle():
    user_profile = {
        "age": 62,
        "dependents": 2,
        "income": 0,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user_dto = UserProfileDTO(**user_profile)
    user_base_risk = UserProfileRisk(user_dto)
    rule = HasNoVehicle() | HasVehicle
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User should not be eligible to disability
    assert risk.disability.risk == 2
    assert risk.auto.is_eligible == False
    assert risk.home.risk == 2
    assert risk.life.risk == 2


def test_new_vehicle():
    # HasNewVehicle
    user_profile = {
        "age": 62,
        "dependents": 0,
        "income": 220000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
        "vehicle": {"year": 2018},
    }
    user_dto = UserProfileDTO(**user_profile)
    user_base_risk = UserProfileRisk(user_dto)
    rule = HasNoVehicle() | HasVehicle
    risk = rule.apply_rule(user_dto, user_base_risk)
    # All risk lines should be reduced by 1
    assert risk.disability.risk == 2
    assert risk.auto.risk == 3
    assert risk.home.risk == 2
    assert risk.life.risk == 2


def test_no_rule():
    user_profile = {
        "age": 62,
        "dependents": 0,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
        "vehicle": {"year": 2000},
    }
    user_dto = UserProfileDTO(**user_profile)
    user_base_risk = UserProfileRisk(user_dto)
    rule = HasNoVehicle() | HasVehicle
    risk = rule.apply_rule(user_dto, user_base_risk)
    # User risk should not change
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2

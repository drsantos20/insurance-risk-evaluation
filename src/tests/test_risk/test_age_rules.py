from domain.dtos.user_profile import UserProfileDTO
from domain.risk.category.age import (
    AgeBetweenThirtyAndForty, 
    AgeOverSixty,
    AgeUnderThirty,
)
from domain.risk.user_profile_risk import UserProfileRisk


def test_age_over_sixty():
    profile_data = {
        "age": 62,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user1_dto = UserProfileDTO(**profile_data)
    user1_base_risk = UserProfileRisk(user1_dto)
    rule = AgeOverSixty() | AgeBetweenThirtyAndForty | AgeUnderThirty
    risk = rule.apply_rule(user1_dto, user1_base_risk)
    # Should not be eligible to life nor disability
    assert risk.disability.is_eligible == False
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.is_eligible == False


def test_age_under_thirty():
    profile_data = {
        "age": 20,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user2_dto = UserProfileDTO(**profile_data)
    user2_base_risk = UserProfileRisk(user2_dto)
    rule = AgeOverSixty() | AgeBetweenThirtyAndForty | AgeUnderThirty
    risk = rule.apply_rule(user2_dto, user2_base_risk)
    # Should have 2 risk points reduced in all lines
    assert risk.disability.risk == 0
    assert risk.auto.risk == 0
    assert risk.home.risk == 0
    assert risk.life.risk == 0


def test_age_between_thirty_and_forty():
    profile_data = {
        "age": 38,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user3_dto = UserProfileDTO(**profile_data)
    user3_base_risk = UserProfileRisk(user3_dto)
    rule = AgeOverSixty() | AgeBetweenThirtyAndForty | AgeUnderThirty
    risk = rule.apply_rule(user3_dto, user3_base_risk)
    # Should 1 risk point reduced in all lines
    assert risk.disability.risk == 1
    assert risk.auto.risk == 1
    assert risk.home.risk == 1
    assert risk.life.risk == 1


def test_age_no_rule():
    user4_info = {
        "age": 40,
        "dependents": 2,
        "income": 1000,
        "marital_status": "single",
        "risk_questions": [0, 1, 1],
    }
    user4_dto = UserProfileDTO(**user4_info)
    user4_base_risk = UserProfileRisk(user4_dto)
    rule = AgeOverSixty() | AgeBetweenThirtyAndForty | AgeUnderThirty
    risk = rule.apply_rule(user4_dto, user4_base_risk)
    # Should have the same base score
    assert risk.disability.risk == 2
    assert risk.auto.risk == 2
    assert risk.home.risk == 2
    assert risk.life.risk == 2

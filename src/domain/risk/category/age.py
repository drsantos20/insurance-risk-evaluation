from domain.dtos.user_profile import UserProfileDTO
from domain.risk.category.base_rule import BaseRule
from domain.risk.user_profile_risk import UserProfileRisk


class AgeOverSixty(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if user_profile.age > 60:
            user_risk.disability.is_eligible = False
            user_risk.life.is_eligible = False
        return super().apply_rule(user_profile, user_risk)


class AgeUnderThirty(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if user_profile.age < 30:
            user_risk.disability.risk -= 2
            user_risk.auto.risk -= 2
            user_risk.home.risk -= 2
            user_risk.life.risk -= 2
        return super().apply_rule(user_profile, user_risk)


class AgeBetweenThirtyAndForty(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if user_profile.age >= 30 and user_profile.age < 40:
            user_risk.disability.risk -= 1
            user_risk.auto.risk -= 1
            user_risk.home.risk -= 1
            user_risk.life.risk -= 1
        return super().apply_rule(user_profile, user_risk)

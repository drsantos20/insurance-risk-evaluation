from domain.risk.category.base_rule import BaseRule
from domain.dtos.user_profile import UserProfileDTO
from domain.risk.user_profile_risk import UserProfileRisk


class HasNoIncome(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if not user_profile.income:
            user_risk.disability.is_eligible = False
        return super().apply_rule(user_profile, user_risk)


class IncomeEvaluation(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if user_profile.income > 200000:
            user_risk.auto.risk -= 1
            user_risk.disability.risk -= 1
            user_risk.life.risk -= 1
            user_risk.home.risk -= 1
        return super().apply_rule(user_profile, user_risk)

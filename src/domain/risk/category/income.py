from domain.risk.categories.base_rule import BaseRule
from domain.dtos.user_profile import UserProfileDTO
from domain.risk.user_risk import UserRisk


class HasNoIncome(BaseRule):
    def apply_rule(self, user_info: UserProfileDTO, user_risk: UserRisk) -> UserRisk:
        if not user_info.income:
            user_risk.disability.is_eligible = False
        return super().apply_rule(user_info, user_risk)


class IncomeEvaluation(BaseRule):
    def apply_rule(self, user_info: UserProfileDTO, user_risk: UserRisk) -> UserRisk:
        if user_info.income > 200000:
            user_risk.auto.risk -= 1
            user_risk.disability.risk -= 1
            user_risk.life.risk -= 1
            user_risk.home.risk -= 1
        return super().apply_rule(user_info, user_risk)

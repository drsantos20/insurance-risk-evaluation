from domain.dtos.user_profile import UserProfileDTO
from domain.risk.category.base_rule import BaseRule
from domain.risk.user_profile_risk import UserProfileRisk


class HasDependents(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if user_profile.dependents:
            user_risk.disability.risk += 1
            user_risk.life.risk += 1
        return super().apply_rule(user_profile, user_risk)

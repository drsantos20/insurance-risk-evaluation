from domain.dtos.user_profile import UserProfileDTO
from domain.risk.category.base_rule import BaseRule
from domain.risk.user_profile_risk import UserProfileRisk


class HasNoHouse(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if not user_profile.house:
            user_risk.home.is_eligible = False
        return super().apply_rule(user_profile, user_risk)


class HasMotgagedHouse(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if not user_profile.house:
            return super().apply_rule(user_profile, user_risk)

        if user_profile.house["ownership_status"] == "mortgaged":
            user_risk.disability.risk += 1
            user_risk.home.risk += 1
        return super().apply_rule(user_profile, user_risk)

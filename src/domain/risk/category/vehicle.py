from datetime import date

from domain.risk.category.base_rule import BaseRule
from domain.dtos.user_profile import UserProfileDTO
from domain.risk.user_profile_risk import UserProfileRisk


class HasNoVehicle(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        if not user_profile.vehicle:
            user_risk.auto.is_eligible = False
        return super().apply_rule(user_profile, user_risk)


class HasVehicle(BaseRule):
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserProfileRisk) -> UserProfileRisk:
        current_year = date.today().year
        if not user_profile.vehicle:
            return super().apply_rule(user_profile, user_risk)
        if user_profile.vehicle["year"] > current_year - 5:
            user_risk.auto.risk += 1
        return super().apply_rule(user_profile, user_risk)

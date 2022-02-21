from datetime import date

from domain.risk.categories.base_rule import BaseRule
from domain.dtos.user_profile import UserProfileDTO
from domain.risk.user_risk import UserRisk


class HasNoVehicle(BaseRule):
    def apply_rule(self, user_info: UserProfileDTO, user_risk: UserRisk) -> UserRisk:
        if not user_info.vehicle:
            user_risk.auto.is_eligible = False
        return super().apply_rule(user_info, user_risk)


class HasVehicle(BaseRule):
    def apply_rule(self, user_info: UserProfileDTO, user_risk: UserRisk) -> UserRisk:
        current_year = date.today().year
        if not user_info.vehicle:
            return super().apply_rule(user_info, user_risk)
        if user_info.vehicle["year"] > current_year - 5:
            user_risk.auto.risk += 1
        return super().apply_rule(user_info, user_risk)

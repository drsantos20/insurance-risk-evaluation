from abc import ABC, abstractmethod
from domain.risk.user_risk import UserRisk
from domain.dtos.user_profile import UserProfileDTO


class RuleInterface(ABC):
    @abstractmethod
    def apply_rule(self, request) -> UserRisk:
        pass


class BaseRule(RuleInterface):
    """An Abstract Rule"""

    next_rule: RuleInterface = None

    def __init__(self, rule: RuleInterface = None):
        self.next_rule = rule

    def __or__(self, OtherRule: RuleInterface) -> RuleInterface:
        """
        Overload the pipe | operator to chain and extend the risk categories
        """
        return OtherRule(self)

    @abstractmethod
    def apply_rule(self, user_profile: UserProfileDTO, user_risk: UserRisk) -> UserRisk:
        """Apply rule in a chain setting user_risk based on user_profile

        Args:
            user_profile: An object containing user profile
            user_risk: An object containing user risk categories

        Returns:
            An user risk object
        """
        if self.next_rule:
            return self.next_rule.apply_rule(user_profile, user_risk)
        return user_risk

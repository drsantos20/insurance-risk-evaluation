from domain.dtos.user_profile import UserProfileDTO
from domain.dtos.insurance import ScoreEnum, InsuranceDTO


class InsuranceRiskCategory:
    """A InsuranceRiskCategory has two properties: a risk
    (value of the risk) and users eligibility for that category risk item
    """

    risk: int
    is_eligible: bool

    def __init__(self, risk: int, is_eligible: bool) -> None:
        self.risk = risk
        self.is_eligible = is_eligible


class UserProfileRisk:
    """A UserProfileRisk has risk categories for every insurance risk category.
    Risk categories are InsuranceRiskCategory instances.
    """

    def __init__(self, user_profile: UserProfileDTO) -> None:
        # Calculate base risk from user_profile risk_questions
        base_risk = sum([1 if x else 0 for x in user_profile.risk_questions])

        self.auto = InsuranceRiskCategory(base_risk, True)
        self.disability = InsuranceRiskCategory(base_risk, True)
        self.home = InsuranceRiskCategory(base_risk, True)
        self.life = InsuranceRiskCategory(base_risk, True)

    def _score_from_risk_category(self, line: InsuranceRiskCategory) -> ScoreEnum:
        """Method to get risk score (eligible, ineligible, economic, regular, responsible)
        based on risk category value
        """
        if not line.is_eligible:
            return ScoreEnum.ineligible
        if line.risk <= 0:
            return ScoreEnum.economic
        if line.risk <= 2:
            return ScoreEnum.regular
        if line.risk >= 3:
            return ScoreEnum.responsible

    def evaluate_risk_category(self) -> InsuranceDTO:
        """For each insurance risk category evaluate to get risk score
        then, return an InsuranceDTO object
        """
        risk_categories = ["auto", "disability", "home", "life"]
        insurance_dict = dict()
        for risk_categoriy in risk_categories:
            score = self._score_from_risk_category(getattr(self, risk_categoriy))
            insurance_dict[risk_categoriy] = score
        insurance = InsuranceDTO(**insurance_dict)
        return insurance

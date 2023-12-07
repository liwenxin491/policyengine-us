from policyengine_us.model_api import *


class mt_disability_income_subtraction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Montana disability income subtraction"
    defined_for = StateCode.MT
    unit = USD
    definition_period = YEAR
    reference = "https://rules.mt.gov/gateway/RuleNo.asp?RN=42%2E15%2E217"
    adds = ["mt_disability_income_subtraction_person"]

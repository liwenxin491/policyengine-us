from policyengine_us.model_api import *


class mt_disability_income_subtraction_person(Variable):
    value_type = float
    entity = Person
    label = "Montana disability income subtraction at person level"
    defined_for = StateCode.MT
    unit = USD
    definition_period = YEAR
    reference = "https://rules.mt.gov/gateway/RuleNo.asp?RN=42%2E15%2E217"

    def formula(person, period, parameters):
        # first select head and spouse with ages below the specific threshold, and
        # select those who are retired on total disability and disabled, and
        # calculate the corresbonding disability benefits.
        p = parameters(
            period
        ).gov.states.mt.tax.income.subtractions.disability_income
        age_eligible = person("age", period) < p.age_threshold
        head_or_spouse = person("is_tax_unit_head_or_spouse", period)
        is_retired_on_disability = person(
            "retired_on_total_disability", period
        )
        eligible_retiree = age_eligible & is_retired_on_disability
        is_disabled = person("is_disabled", period)
        disabled_retiree = eligible_retiree & is_disabled
        qualified_head_or_spouse = disabled_retiree & head_or_spouse
        eligible_benefits = (
            person("disability_benefits", period) * qualified_head_or_spouse
        )
        return eligible_benefits

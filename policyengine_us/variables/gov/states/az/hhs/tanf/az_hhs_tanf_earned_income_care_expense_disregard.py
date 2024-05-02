from policyengine_us.model_api import *


class az_hhs_tanf_earned_income_care_expense_disregard(Variable):
    value_type = float
    entity = SPMUnit
    label = "Arizona Cash Assistance care expense earned income disregard"
    definition_period = MONTH
    defined_for = StateCode.AZ

    def formula(spm_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.az.hhs.tanf.eligibility.income.earned.care_expenses
        # Get the age of the child(children) and the disabled adult(s)
        person = spm_unit.members
        age = person("age", period)
        # Get the childcare and disabled adult care expenses
        care_expenses = spm_unit("childcare_expenses", period)
        monthly_care_expenses = care_expenses / MONTHS_IN_YEAR
        # Determine the total eligible disregard
        # The eligibility reuquirements consider wither children or disabled adults
        #young_eligible_child = age < p.child_age
        #is_child = person("az_tanf_eligible_child", period)
        disabled_adult = person("is_disabled", period)
        child_amount=p.child_amounts.calc(age)
        print(child_amount)
        adult_amount = disabled_adult * p.adult  
        total_amount = child_amount + adult_amount
        # disregard_amount = select(
        #     [
        #         young_eligible_child,
        #         is_child,
        #         disabled_adult,
        #     ],
        #     [
        #         p.younger,
        #         p.older,
        #         p.adult,
        #     ],
        #     default=0,
        # )
        #total_disregard = spm_unit.sum(disregard_amount)

        # The disregard is capped at the expenses
        return min_(monthly_care_expenses, total_amount)

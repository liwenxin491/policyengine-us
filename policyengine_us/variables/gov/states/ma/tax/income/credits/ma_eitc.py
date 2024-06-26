from policyengine_us.model_api import *


class ma_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "MA EITC"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.mass.gov/info-details/mass-general-laws-c62-ss-6"  # (h)
    )
    defined_for = StateCode.MA

    def formula(tax_unit, period, parameters):
        federal_eitc = tax_unit("eitc", period)
        rate = parameters(period).gov.states.ma.tax.income.credits.eitc.match
        return federal_eitc * rate

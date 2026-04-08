"""
File Name: HoweLab2.py
Purpose: Simulate an investment outcome using a simple formula with variables and expressions.
Problem description: Calculate ending value, total contributions, total dividends generated, and ROI under stated assumptions.
First created date: 2026-01-26
Author: Daniel Howe
Version: 1.5
"""

# -------------------------
# Constants (avoid magic numbers)
# -------------------------
MONTHS_PER_YEAR: int = 12       # int, months in one year
PERCENT_SCALE: float = 100.0    # float, converts ratio to percent

# -------------------------
# Required Inputs (variables initialized at the beginning)
# -------------------------
investor_name: str = "Daniel Howe"      # str, investor name
initial_investment: float = 10000.0     # float, starting deposit in dollars
monthly_contribution: float = 500.0     # float, monthly added amount in dollars
annual_growth_rate: float = 0.06        # float, annual growth rate as a decimal (e.g., 0.06 = 6%)
annual_dividend_yield: float = 0.03     # float, annual dividend yield as a decimal (e.g., 0.03 = 3%)
years: int = 30                         # int, number of years invested

# -------------------------
# Assumptions (printed as part of output)
# -------------------------
assumption_1: str = "Initial investment earns growth/dividends for the full term."                              # str, assumption text
assumption_2: str = "Monthly contributions earn growth/dividends for an average (mid-period) time in market."   # str, assumption text
assumption_3: str = "Growth and dividends use simple rates over time (no compounding)."                         # str, assumption text

# -------------------------
# Calculations (expressions using variables)
# -------------------------
total_months: int = years * MONTHS_PER_YEAR                                   # int, total months in the term
monthly_contributions_total: float = monthly_contribution * total_months      # float, total dollars contributed (excluding initial)
total_contributions: float = initial_investment + monthly_contributions_total # float, total dollars contributed (initial + monthly)

# Mid-period approximation:
# Average contribution dollar is invested for about half the total time horizon.
average_contribution_years: float = years / 2.0                               # float, average years that contributed dollars are invested

# Growth/dividends on initial investment for full term (simple, no compounding)
growth_initial: float = initial_investment * annual_growth_rate * years       # float, growth gained on initial investment
dividends_initial: float = initial_investment * annual_dividend_yield * years # float, dividends earned on initial investment

# Growth/dividends on contributions for average time in market (simple, no compounding)
growth_contrib: float = monthly_contributions_total * annual_growth_rate * average_contribution_years       # float, growth gained on contributed dollars
dividends_contrib: float = monthly_contributions_total * annual_dividend_yield * average_contribution_years # float, dividends earned on contributed dollars

# Totals (simple, no compounding)
growth_gain: float = growth_initial + growth_contrib                          # float, total growth gain (initial + contributions)
dividend_gain: float = dividends_initial + dividends_contrib                  # float, total dividend gain (initial + contributions)

ending_invested_balance: float = total_contributions + growth_gain            # float, balance after adding growth (no compounding)
ending_total_value: float = ending_invested_balance + dividend_gain           # float, final value after adding dividends (no compounding)

# -------------------------
# ROI Calculation (with divide-by-zero guard)
# -------------------------
roi_ratio: float = 0.0                                                        # float, ROI as a ratio (default if divide-by-zero would occur)
if total_contributions > 0:                                                   # guard, prevent divide-by-zero
    roi_ratio = (ending_total_value - total_contributions) / total_contributions  # float, ROI ratio = net gain / contributions

roi_percent: float = roi_ratio * PERCENT_SCALE                                # float, ROI expressed as a percent

# -------------------------
# Output (complete sentence; values represented by variables)
# -------------------------
initial_investment_str: str = "${0:,.2f}".format(initial_investment)          # str, formatted initial investment dollars
monthly_contribution_str: str = "${0:,.2f}".format(monthly_contribution)      # str, formatted monthly contribution dollars
total_contributions_str: str = "${0:,.2f}".format(total_contributions)        # str, formatted total contributions dollars
total_dividends_str: str = "${0:,.2f}".format(dividend_gain)                  # str, formatted total dividends dollars
ending_total_value_str: str = "${0:,.2f}".format(ending_total_value)          # str, formatted ending total value dollars
roi_percent_str: str = "{0:.2f}%".format(roi_percent)                         # str, formatted ROI percent

assumptions_str: str = assumption_1 + " " + assumption_2 + " " + assumption_3 # str, combined assumptions text

output_sentence: str = (                                                      # str, final output sentence describing results
    investor_name + " invested " + initial_investment_str + " initially and contributed " +
    monthly_contribution_str + " per month for " + str(years) + " years; total contributions were " +
    total_contributions_str + ", total dividends were " + total_dividends_str + ", ending value was " +
    ending_total_value_str + ", and ROI was " + roi_percent_str + " (" + assumptions_str + ")."
)

print(output_sentence)                                                        # print, displays the complete sentence output





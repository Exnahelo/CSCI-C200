"""
File Name: HoweLab3.py
Purpose: Collect yield data, compute Treasury vs. Corporate spreads, summarize results, and estimate simple interest.
Problem description: Gather multi-year yield inputs, compute spread per year (corporate - treasury), compute spread stats (avg/min/max), then estimate simple interest using average corporate yield.
First created date: 2026-02-02
Author: Daniel Howe
Version: 1.0
"""


# -------------------------
# Constants (avoid magic numbers)
# -------------------------
PERCENT_SCALE: float = 100.0           # float, converts percent to decimal by dividing (rate_percent / 100)
MIN_YEARS_DATA: int = 1                # int, minimum number of yearly entries required
MIN_YEAR_VALUE: int = 1                # int, minimum allowed calendar year input (simple guard)
MIN_YIELD_PERCENT: float = 0.0         # float, minimum allowed yield percentage
MIN_PRINCIPAL: float = 0.0             # float, minimum allowed principal
MIN_INVEST_YEARS: int = 1              # int, minimum allowed investment duration (years)


# -------------------------
# Required Inputs / Data Storage (initialized at the beginning)
# -------------------------
# The program uses parallel lists so that index i refers to the same "row" of data across lists.
# Example: year_list[i], treasury_yields[i], corporate_yields[i], spreads[i] all describe the i-th year entry.
user_name: str = ""                    # str, optional user name for output label
num_years: int = 0                     # int, number of year entries the user will provide

year_list: list[int] = []              # list[int], calendar years entered by the user
treasury_yields: list[float] = []      # list[float], treasury yields (percent values, e.g., 4.25 means 4.25%)
corporate_yields: list[float] = []     # list[float], corporate yields (percent values)
spreads: list[float] = []              # list[float], computed spreads in percentage points (pp)


# -------------------------
# Summary Results (computed later)
# -------------------------
avg_spread: float = 0.0                # float, average spread (pp) across all entered years
min_spread: float = 0.0                # float, minimum spread (pp)
max_spread: float = 0.0                # float, maximum spread (pp)


# -------------------------
# Investment Estimate Inputs/Outputs (computed later)
# -------------------------
principal: float = 0.0                 # float, principal amount in dollars for simple interest estimate
investment_years: int = 0              # int, investment duration in years for simple interest estimate
avg_corporate_yield: float = 0.0       # float, average corporate yield (%) used as the interest rate
interest_earned: float = 0.0           # float, simple interest earned in dollars


# -------------------------
# Function Definitions (utilities + computations)
# -------------------------
def get_int(prompt: str, min_value: int) -> int:
    """
    Purpose:
        Prompt the user for an integer and validate it.

    Parameters:
        prompt (str): text shown to the user
        min_value (int): minimum allowed value (inclusive)

    Returns:
        int: a validated integer >= min_value

    Notes:
        - Re-prompts on invalid input (non-integer or below minimum).
        - Centralizes input validation to keep the main program readable.
    """
    while True:
        user_input: str = input(prompt)                # str, raw input from user
        try:
            value: int = int(user_input)               # int, attempted conversion
            if value < min_value:
                print(f"Value must be at least {min_value}. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid integer. Try again.")


def get_float(prompt: str, min_value: float) -> float:
    """
    Purpose:
        Prompt the user for a float and validate it.

    Parameters:
        prompt (str): text shown to the user
        min_value (float): minimum allowed value (inclusive)

    Returns:
        float: a validated float >= min_value

    Notes:
        - Re-prompts on invalid input (non-number or below minimum).
        - Expects yields as percent values, not decimals (e.g., 4.25 not 0.0425).
    """
    while True:
        user_input: str = input(prompt)                # str, raw input from user
        try:
            value: float = float(user_input)           # float, attempted conversion
            if value < min_value:
                print(f"Value must be at least {min_value}. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid number. Try again.")


def compute_spread(treasury_yield_percent: float, corporate_yield_percent: float) -> float:
    """
    Purpose:
        Compute yield spread in percentage points (pp).

    Parameters:
        treasury_yield_percent (float): treasury yield in percent (e.g., 4.25 means 4.25%)
        corporate_yield_percent (float): corporate yield in percent

    Returns:
        float: spread (pp) = corporate_yield_percent - treasury_yield_percent

    Example:
        treasury = 4.50
        corporate = 6.00
        spread = 1.50 pp
    """
    spread_pp: float = corporate_yield_percent - treasury_yield_percent   # float, percentage points
    return spread_pp


def compute_stats(values: list[float]) -> tuple[float, float, float]:
    """
    Purpose:
        Compute average, minimum, and maximum of a numeric list.

    Parameters:
        values (list[float]): list of numeric values (must be non-empty)

    Returns:
        tuple[float, float, float]: (average, minimum, maximum)

    Notes:
        - This program guarantees the list is non-empty because num_years >= 1.
        - Average is computed manually (loop) to reinforce core programming concepts.
    """
    total: float = 0.0                                  # float, running total for average
    for v in values:
        total += v

    average: float = total / len(values)                # float, mean of list
    minimum: float = min(values)                        # float, smallest value
    maximum: float = max(values)                        # float, largest value
    return average, minimum, maximum


def simple_interest(principal_amount: float, rate_percent: float, years_count: int) -> float:
    """
    Purpose:
        Compute simple interest earned (no compounding).

    Parameters:
        principal_amount (float): principal in dollars
        rate_percent (float): annual interest rate in percent (e.g., 5.0 means 5%)
        years_count (int): number of years invested

    Returns:
        float: interest earned in dollars

    Formula:
        interest = principal_amount * (rate_percent / 100) * years_count

    Notes:
        - This returns interest earned only (not ending balance).
        - This uses a percent-to-decimal conversion (rate_percent / 100).
    """
    interest: float = principal_amount * (rate_percent / PERCENT_SCALE) * years_count
    return interest


# -------------------------
# Input Block (Keyboard Entry)
# -------------------------
# Collect user name (optional), number of year entries, and yield data per year.
print("Yield Spread Analyzer")
print("---------------------")

user_name = input("Enter your name: ").strip()          # str, optional name for output labeling

num_years = get_int(
    "Enter number of years of yield data (>= 1): ",
    MIN_YEARS_DATA
)

# Loop to collect each year's yield data and store in parallel lists.
for i in range(num_years):
    print(f"\nEntry {i + 1} of {num_years}")

    year_value: int = get_int("  Enter year (e.g., 2024): ", MIN_YEAR_VALUE)
    treasury: float = get_float("  Enter Treasury yield (%) (>= 0): ", MIN_YIELD_PERCENT)
    corporate: float = get_float("  Enter Corporate yield (%) (>= 0): ", MIN_YIELD_PERCENT)

    year_list.append(year_value)
    treasury_yields.append(treasury)
    corporate_yields.append(corporate)


# -------------------------
# Main Computation Block
# -------------------------
# Compute the spread for each year entry and store it for reporting and summary stats.
for i in range(num_years):
    spread_value: float = compute_spread(treasury_yields[i], corporate_yields[i])
    spreads.append(spread_value)

# Compute spread summary statistics for output.
avg_spread, min_spread, max_spread = compute_stats(spreads)


# -------------------------
# Investment Block (Simple Interest Estimate)
# -------------------------
# This section estimates interest earned using:
#   - user-provided principal
#   - average corporate yield from the entered data
#   - user-provided investment duration
print("\nInvestment Estimate (Simple Interest)")

principal = get_float("Enter principal amount ($) (>= 0): ", MIN_PRINCIPAL)
investment_years = get_int("Enter investment years (>= 1): ", MIN_INVEST_YEARS)

avg_corporate_yield, _, _ = compute_stats(corporate_yields)                  # avg corporate yield (%)
interest_earned = simple_interest(principal, avg_corporate_yield, investment_years)


# -------------------------
# Output Block (Meaningful Output)
# -------------------------
# Prints a table of yearly inputs and spreads, then prints summary stats and investment estimate.
print("\nResults")
print("-------")

# Show user name if provided; otherwise, label as missing.
if user_name:
    print(f"User: {user_name}")
else:
    print("User: (no name entered)")

# Table header for the yearly yield/spread results.
print("\nYear | Treasury Yield (%) | Corporate Yield (%) | Spread (pp)")
print("-----|---------------------|--------------------|-----------")

# Print each year's yields and computed spread.
# Formatting details:
#   - Year is printed as a 4-digit integer
#   - Yields/spread are printed with 2 decimal places
for i in range(num_years):
    print(
        f"{year_list[i]:4d} | {treasury_yields[i]:19.2f} | "
        f"{corporate_yields[i]:18.2f} | {spreads[i]:9.2f}"
    )

# Spread summary section.
print("\nSpread Summary (percentage points)")
print(f"  Average spread: {avg_spread:.2f} pp")
print(f"  Minimum spread: {min_spread:.2f} pp")
print(f"  Maximum spread: {max_spread:.2f} pp")

# Simple interest estimate section.
print("\nSimple Interest Estimate")
print(f"  Principal: ${principal:,.2f}")
print(f"  Avg Corporate Yield Used: {avg_corporate_yield:.2f}%")
print(f"  Years: {investment_years}")
print(f"  Estimated Interest Earned: ${interest_earned:,.2f}")

print("\nDone.")
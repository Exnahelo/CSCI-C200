"""
Project Name: CodexUtil.py (utility module)
Purpose: Provide budget category evaluation helpers.
Author: Daniel Howe
Version: 1.3
"""

# Housing percent-of-income thresholds
HOUSING_LOW_MAX = 0.25
HOUSING_TYPICAL_MAX = 0.35

# Food percent-of-income thresholds
FOOD_LOW_MAX = 0.09
FOOD_TYPICAL_MAX = 0.15

# Transportation percent-of-income thresholds
TRANSPORT_LOW_MAX = 0.08
TRANSPORT_TYPICAL_MAX = 0.14

# Entertainment percent-of-income thresholds
ENTERTAINMENT_LOW_MAX = 0.04
ENTERTAINMENT_TYPICAL_MAX = 0.09

# Savings percent-of-income thresholds
SAVINGS_LOW_MAX = 0.10
SAVINGS_TYPICAL_MAX = 0.20


def _evaluate_level(percent_of_income, low_max, typical_max):
    """Classify a spending ratio as Low, Typical, or High.

    Args:
        percent_of_income: Spending ratio as a decimal (e.g., 0.25 for 25%).
        low_max: Inclusive upper bound for the Low label.
        typical_max: Inclusive upper bound for the Typical label.

    Returns:
        A string classification: "Low", "Typical", or "High".
    """
    # First decision: spending is at or below the low cutoff.
    if percent_of_income <= low_max:
        return "Low"

    # Second decision: spending is above low but still within the typical range.
    if percent_of_income <= typical_max:
        return "Typical"

    # Any value above the typical upper bound is high.
    return "High"


def evaluate_housing(percent_of_income):
    """Evaluate housing spending ratio and return Low, Typical, or High."""
    return _evaluate_level(percent_of_income, HOUSING_LOW_MAX, HOUSING_TYPICAL_MAX)


def evaluate_food(percent_of_income):
    """Evaluate food spending ratio and return Low, Typical, or High."""
    return _evaluate_level(percent_of_income, FOOD_LOW_MAX, FOOD_TYPICAL_MAX)


def evaluate_transportation(percent_of_income):
    """Evaluate transportation spending ratio and return Low, Typical, or High."""
    return _evaluate_level(percent_of_income, TRANSPORT_LOW_MAX, TRANSPORT_TYPICAL_MAX)


def evaluate_entertainment(percent_of_income):
    """Evaluate entertainment spending ratio and return Low, Typical, or High."""
    return _evaluate_level(percent_of_income, ENTERTAINMENT_LOW_MAX, ENTERTAINMENT_TYPICAL_MAX)


def evaluate_savings(percent_of_income):
    """Evaluate savings ratio and return Low, Typical, or High."""
    return _evaluate_level(percent_of_income, SAVINGS_LOW_MAX, SAVINGS_TYPICAL_MAX)

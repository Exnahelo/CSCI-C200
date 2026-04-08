"""
Project: HoweLab5Util.py
Purpose: Category evaluator functions that classify percent-of-income values as
         "Low", "Typical", or "High" based on predefined thresholds.
Author: Daniel Howe
Created: 2026-02-16
Version: 2.1
Notes:
- No input() and no print() in this file.
- All public functions return ONLY: "Low" | "Typical" | "High"
- Assumes percent_of_income is a ratio (e.g., 0.25 = 25%).
"""

# ============================================================
# ---- Threshold Constants ----
# ============================================================
HOUSING_LOW_MAX = 0.25
HOUSING_TYPICAL_MAX = 0.35

FOOD_LOW_MAX = 0.09
FOOD_TYPICAL_MAX = 0.15

TRANSPORT_LOW_MAX = 0.08
TRANSPORT_TYPICAL_MAX = 0.14

ENT_LOW_MAX = 0.04
ENT_TYPICAL_MAX = 0.09

SAVINGS_LOW_MAX = 0.10
SAVINGS_TYPICAL_MAX = 0.20


# ============================================================
# ---- Internal Helper ----
# ============================================================
def _classify(percent_of_income: float, low_max: float, typical_max: float) -> str:
    """
    Classify percent_of_income into "Low", "Typical", or "High" given thresholds.

    Policy:
    - percent_of_income <= low_max        -> "Low"
    - percent_of_income <= typical_max    -> "Typical"
    - otherwise                           -> "High"
    """
    if percent_of_income <= low_max:
        return "Low"
    elif percent_of_income <= typical_max:
        return "Typical"
    return "High"


# ============================================================
# ---- Evaluator Functions ----
# ============================================================
def evaluate_housing(percent_of_income: float) -> str:
    """Classify housing spend as Low/Typical/High using fixed thresholds."""
    return _classify(percent_of_income, HOUSING_LOW_MAX, HOUSING_TYPICAL_MAX)


def evaluate_food(percent_of_income: float) -> str:
    """Classify food spend as Low/Typical/High using fixed thresholds."""
    return _classify(percent_of_income, FOOD_LOW_MAX, FOOD_TYPICAL_MAX)


def evaluate_transportation(percent_of_income: float) -> str:
    """Classify transportation spend as Low/Typical/High using fixed thresholds."""
    return _classify(percent_of_income, TRANSPORT_LOW_MAX, TRANSPORT_TYPICAL_MAX)


def evaluate_entertainment(percent_of_income: float) -> str:
    """Classify entertainment spend as Low/Typical/High using fixed thresholds."""
    return _classify(percent_of_income, ENT_LOW_MAX, ENT_TYPICAL_MAX)


def evaluate_savings(percent_of_income: float) -> str:
    """
    Classify savings rate as Low/Typical/High using fixed thresholds.

    Note: "High" here is a strong savings rate (positive outcome), not overspending.
    """
    return _classify(percent_of_income, SAVINGS_LOW_MAX, SAVINGS_TYPICAL_MAX)


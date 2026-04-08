"""
Project: HoweUtil.py
Purpose: Category evaluators that classify percent-of-income as Low/Typical/High.
Author: Daniel Howe
Created: 2026-02-09
Version: 1.3
Notes:
- No input() and no print() in this file.
- All functions return ONLY: "Low" | "Typical" | "High"
"""

# ---- Threshold constants (no magic numbers in logic) ----
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


def evaluate_housing(percent_of_income: float) -> str:
    """Classify housing spend as Low/Typical/High using fixed thresholds."""
    if percent_of_income <= HOUSING_LOW_MAX:
        return "Low"
    elif percent_of_income <= HOUSING_TYPICAL_MAX:
        return "Typical"
    else:
        return "High"


def evaluate_food(percent_of_income: float) -> str:
    """Classify food spend as Low/Typical/High using fixed thresholds."""
    if percent_of_income <= FOOD_LOW_MAX:
        return "Low"
    elif percent_of_income <= FOOD_TYPICAL_MAX:
        return "Typical"
    else:
        return "High"


def evaluate_transportation(percent_of_income: float) -> str:
    """Classify transportation spend as Low/Typical/High using fixed thresholds."""
    if percent_of_income <= TRANSPORT_LOW_MAX:
        return "Low"
    elif percent_of_income <= TRANSPORT_TYPICAL_MAX:
        return "Typical"
    else:
        return "High"


def evaluate_entertainment(percent_of_income: float) -> str:
    """Classify entertainment spend as Low/Typical/High using fixed thresholds."""
    if percent_of_income <= ENT_LOW_MAX:
        return "Low"
    elif percent_of_income <= ENT_TYPICAL_MAX:
        return "Typical"
    else:
        return "High"


def evaluate_savings(percent_of_income: float) -> str:
    """
    Classify savings rate as Low/Typical/High using fixed thresholds.
    Note: "High" here is a strong savings rate (positive outcome), not overspending.
    """
    if percent_of_income <= SAVINGS_LOW_MAX:
        return "Low"
    elif percent_of_income <= SAVINGS_TYPICAL_MAX:
        return "Typical"
    else:
        return "High"

"""
Project: HoweUtil.py
Purpose: Category evaluators that classify percent-of-income as Low/Typical/High.
Author: Daniel Howe
Created: 2026-02-09
Version: 1.3
"""


def evaluate_housing(percent_of_income):
    """Evaluate housing spending percentage against common budget ranges."""
    if percent_of_income < 25:
        return "Low"
    if percent_of_income <= 35:
        return "Typical"
    return "High"


def evaluate_transportation(percent_of_income):
    """Evaluate transportation spending percentage against common budget ranges."""
    if percent_of_income < 10:
        return "Low"
    if percent_of_income <= 15:
        return "Typical"
    return "High"


def evaluate_food(percent_of_income):
    """Evaluate food spending percentage against common budget ranges."""
    if percent_of_income < 8:
        return "Low"
    if percent_of_income <= 15:
        return "Typical"
    return "High"


def evaluate_savings(percent_of_income):
    """Evaluate savings rate percentage against common budget ranges."""
    if percent_of_income < 10:
        return "Low"
    if percent_of_income <= 20:
        return "Typical"
    return "High"
"""
File: budget_utils.py
Author: Cash-Flow-Joe Student
Course: Lab 4 - Conditional Executions
Description:
    Utility functions for analyzing monthly spending in budget categories.
    Each function returns a rating string (low/moderate/high) and a short
    explanation for the selected category.
"""


def analyze_housing(spending_amount: float) -> str:
    """Analyze housing spending level."""
    if spending_amount < 800:
        return "low for Housing"
    if spending_amount <= 1800:
        return "moderate for Housing"
    return "high for Housing"


def analyze_food(spending_amount: float) -> str:
    """Analyze food spending level."""
    if spending_amount < 250:
        return "low for Food"
    if spending_amount <= 700:
        return "moderate for Food"
    return "high for Food"


def analyze_transportation(spending_amount: float) -> str:
    """Analyze transportation spending level."""
    if spending_amount < 150:
        return "low for Transportation"
    if spending_amount <= 500:
        return "moderate for Transportation"
    return "high for Transportation"


def analyze_entertainment(spending_amount: float) -> str:
    """Analyze entertainment spending level."""
    if spending_amount < 100:
        return "low for Entertainment"
    if spending_amount <= 400:
        return "moderate for Entertainment"
    return "high for Entertainment"


def get_analysis_result(category_choice: str, spending_amount: float) -> str:
    """Route category choice to the proper analyzer function."""
    if category_choice == "1":
        return analyze_housing(spending_amount)
    if category_choice == "2":
        return analyze_food(spending_amount)
    if category_choice == "3":
        return analyze_transportation(spending_amount)
    if category_choice == "4":
        return analyze_entertainment(spending_amount)

    # Defensive fallback (main program already validates choices)
    return "invalid category"
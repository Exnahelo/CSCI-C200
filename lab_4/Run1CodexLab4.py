"""
Project Name: CodexLab4.py
Purpose: Help a user categorize a spending amount and receive a quick evaluation based on a selected budget category.
Project Description: This program helps users evaluate how a specific category of monthly spending compares to recommended budgeting guidelines by calculating the percent of income spent and classifying it as Low, Typical, or High.
File Created Date: 2026-02-09
Author: Daniel Howe
Version: 1.3
"""

from CodexUtil import (
    evaluate_entertainment,
    evaluate_food,
    evaluate_housing,
    evaluate_savings,
    evaluate_transportation,
)


MENU_OPTIONS = {
    1: "Housing",
    2: "Food",
    3: "Transportation",
    4: "Entertainment",
    5: "Savings",
    6: "Exit",
}


# The dictionary is the single source of truth for menu display, validation, and output labeling.


def parse_float(raw_value):
    """Convert a raw string into a float value or return None if invalid.

    Args:
        raw_value: User-entered text expected to represent a number.

    Returns:
        A float when conversion succeeds, otherwise None.
    """
    if raw_value is None or raw_value.strip() == "":
        return None

    try:
        return float(raw_value)
    except ValueError:
        return None


def parse_int(raw_value):
    """Convert a raw string into an int value or return None if invalid.

    Args:
        raw_value: User-entered text expected to represent an integer.

    Returns:
        An int when conversion succeeds, otherwise None.
    """
    if raw_value is None or raw_value.strip() == "":
        return None

    try:
        return int(raw_value)
    except ValueError:
        return None


def display_menu():
    """Print the category menu using MENU_OPTIONS."""
    print("\nBudget Categories")
    for key, label in MENU_OPTIONS.items():
        print(f"  {key}. {label}")


def evaluate_category(choice, percent_of_income):
    """Route category choice to the corresponding evaluator.

    Args:
        choice: Integer menu selection.
        percent_of_income: Spending ratio as a decimal.

    Returns:
        Evaluation label as "Low", "Typical", or "High".
    """
    # Route the computed percent to the matching category evaluator.
    if choice == 1:
        return evaluate_housing(percent_of_income)
    if choice == 2:
        return evaluate_food(percent_of_income)
    if choice == 3:
        return evaluate_transportation(percent_of_income)
    if choice == 4:
        return evaluate_entertainment(percent_of_income)
    if choice == 5:
        return evaluate_savings(percent_of_income)

    return None


def main():
    """Run the budget-category spending evaluation workflow."""
    print("Monthly Budget Category Evaluator")
    print("Compare one spending category against generalized budgeting guidelines.")

    run_again = True  # True means start/continue another evaluation cycle; False means stop.

    while run_again:
        # --- Input collection: monthly income ---
        monthly_income_input = input("\nEnter your monthly income: ")  # Raw text entered for income.
        monthly_income = parse_float(monthly_income_input)  # Parsed numeric income value.

        # Validate income presence, type, and positive range.
        if monthly_income is None or monthly_income <= 0:
            print("Error: Monthly income must be a numeric value greater than 0.")
            return

        # --- Input collection: category choice ---
        display_menu()
        choice_input = input("Select a category (1-6): ")  # Raw text menu choice.
        choice = parse_int(choice_input)  # Parsed integer category selection.

        # Validate that the choice is an integer key from MENU_OPTIONS.
        if choice is None or choice not in MENU_OPTIONS:
            print("Error: Menu choice must be a valid integer option from the menu.")
            return

        # Exit path: no category evaluation needed.
        if choice == 6:
            print("Exiting program. Goodbye!")
            return

        selected_category = MENU_OPTIONS[choice]  # Human-readable label for output and prompts.

        # --- Input collection: spending amount for selected category ---
        spending_input = input(f"Enter monthly spending for {selected_category}: ")  # Raw spending text.
        spending_amount = parse_float(spending_input)  # Parsed numeric spending value.

        # Validate spending is numeric, non-negative, and not greater than income.
        if spending_amount is None or spending_amount < 0:
            print("Error: Spending amount must be a numeric value greater than or equal to 0.")
            return
        if spending_amount > monthly_income:
            print("Error: Spending amount cannot be greater than monthly income.")
            return

        # --- Processing and routing ---
        percent_of_income = spending_amount / monthly_income  # Decimal ratio of spending relative to income.
        evaluation_result = evaluate_category(choice, percent_of_income)  # Category evaluation label.

        # --- Output formatting ---
        print("\nEvaluation Result")
        print(f"Category: {selected_category}")
        print(f"Spending: ${spending_amount:,.2f}")
        print(f"Income: ${monthly_income:,.2f}")
        print(f"Percent of Income: {percent_of_income * 100:.2f}%")
        print(f"Evaluation: {evaluation_result}")
        if choice == 5 and evaluation_result == "High":
            print("Note: High savings indicates a strong savings rate.")

        # --- Run-again decision ---
        run_again_input = input("\nRun again? (y/yes to continue): ").strip().lower()  # Loop control input text.
        run_again = run_again_input in {"y", "yes"}  # True loops; False exits.

    print("Program ended.")


if __name__ == "__main__":
    main()
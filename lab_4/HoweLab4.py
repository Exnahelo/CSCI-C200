"""
Project Name: HoweLab4.py
Purpose: Help a user categorize a spending amount and receive a quick evaluation based on a selected budget category.
Description: Prompts for monthly income, category choice, and category spending. Validates inputs (empty/numeric/range) and exits on invalid per spec. Computes percent-of-income and routes to a category evaluator in HoweUtil.py. Prints formatted results; optionally runs again.
File Created Date: 2026-02-09
Author: Daniel Howe
Version: 1.3
"""
import sys
import HoweUtil

# ---- Constants (magic numbers / fixed strings) ----
EXIT_CHOICE = 6  # Menu option number that exits the program

# MENU_OPTIONS: single source of truth for menu display, validation, and output labeling.
MENU_OPTIONS = {
    1: "Housing",
    2: "Food",
    3: "Transportation",
    4: "Entertainment",
    5: "Savings",
    EXIT_CHOICE: "Exit",
}


def _fail_and_exit(message: str) -> None:
    """Print a single error message and exit the program (locked behavior)."""
    print(f"ERROR: {message}")
    sys.exit(1)  # nonzero exit code indicates an error


def get_valid_income() -> float:
    """
    Prompt once for monthly income and validate.
    Returns: income as float (> 0)
    Exits on invalid input (empty, non-numeric, <= 0).
    """
    monthly_income_str = input("Enter your monthly income: ").strip()
    if monthly_income_str == "":
        _fail_and_exit("Monthly income cannot be empty.")

    try:
        monthly_income = float(monthly_income_str)
    except ValueError:
        _fail_and_exit("Monthly income must be numeric.")

    if monthly_income <= 0:
        _fail_and_exit("Monthly income must be greater than 0.")

    return monthly_income


def get_valid_choice() -> int:
    """
    Prompt once for menu choice and validate.
    Returns: choice as int (must be a key in MENU_OPTIONS)
    Exits on invalid input (empty, non-integer, not in MENU_OPTIONS).
    """
    choice_str = input("Select a category (enter the number): ").strip()
    if choice_str == "":
        _fail_and_exit("Menu choice cannot be empty.")

    try:
        choice = int(choice_str)
    except ValueError:
        _fail_and_exit("Menu choice must be an integer.")

    if choice not in MENU_OPTIONS:
        _fail_and_exit("Invalid menu choice.")

    return choice


def get_valid_spending(monthly_income: float, category_label: str) -> float:
    """
    Prompt once for category spending and validate.
    Inputs:
      - monthly_income: used to enforce spending <= income (locked policy)
      - category_label: used to personalize the prompt
    Returns: spending as float (>= 0 and <= income)
    Exits on invalid input (empty, non-numeric, < 0, > income).
    """
    spending_str = input(f"Enter your monthly spending for {category_label}: ").strip()
    if spending_str == "":
        _fail_and_exit("Category spending cannot be empty.")

    try:
        spending_amount = float(spending_str)
    except ValueError:
        _fail_and_exit("Category spending must be numeric.")

    if spending_amount < 0:
        _fail_and_exit("Category spending must be 0 or greater.")

    if spending_amount > monthly_income:
        _fail_and_exit("Category spending cannot exceed monthly income (locked policy).")

    return spending_amount


def print_menu() -> None:
    """Print the category menu using MENU_OPTIONS."""
    print("\nBudget Categories:")
    for key in sorted(MENU_OPTIONS.keys()):
        print(f"  {key}. {MENU_OPTIONS[key]}")


def route_evaluation(choice: int, percent_of_income: float) -> str:
    """
    Route to the correct evaluator based on choice.
    Returns: "Low" | "Typical" | "High"
    """
    # Choice → evaluator mapping:
    # 1: evaluate_housing, 2: evaluate_food, 3: evaluate_transportation,
    # 4: evaluate_entertainment, 5: evaluate_savings

    # Routing decision: rubric-friendly if/elif
    if choice == 1:
        return HoweUtil.evaluate_housing(percent_of_income)
    elif choice == 2:
        return HoweUtil.evaluate_food(percent_of_income)
    elif choice == 3:
        return HoweUtil.evaluate_transportation(percent_of_income)
    elif choice == 4:
        return HoweUtil.evaluate_entertainment(percent_of_income)
    elif choice == 5:
        return HoweUtil.evaluate_savings(percent_of_income)

    _fail_and_exit("Unexpected routing state.")


def main() -> None:
    """Main program flow: inputs → validation → compute → route → output → optional repeat."""
    print("HoweLab4 — Budget Category Evaluator")
    print("Evaluate a category’s monthly spend as a percent of income (Low/Typical/High).")

    # --- Variable Initialization Block ---
    run_again = True  # True = repeat; False = end

    while run_again:
        monthly_income = get_valid_income()

        print_menu()
        choice = get_valid_choice()

        if choice == EXIT_CHOICE:
            print("Exiting. Goodbye.")
            sys.exit(0)

        category_label = MENU_OPTIONS[choice]
        spending_amount = get_valid_spending(monthly_income, category_label)

        percent_of_income = spending_amount / monthly_income  # do NOT round before classification
        evaluation_result = route_evaluation(choice, percent_of_income)

        print("\nResult")
        print("-" * 40)
        print(f"Category:         {category_label}")
        print(f"Monthly Income:   ${monthly_income:,.2f}")
        print(f"Category Spend:   ${spending_amount:,.2f}")
        print(f"Percent of Income:{percent_of_income * 100:>10.2f}%")
        print(f"Evaluation:       {evaluation_result}")

        again_str = input("\nRun again? (Y/N): ").strip().lower()
        run_again = again_str in {"y", "yes"}  # accepts y/yes; everything else ends

    print("Done. Goodbye.")


if __name__ == "__main__":
    main()

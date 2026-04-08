"""
Project Name: HoweLab4.py
Purpose: Help a user categorize a spending amount and receive a quick evaluation
         based on a selected budget category.
Description: Prompts for monthly income, category choice, and category spending.
             Validates inputs (empty/numeric/range) and exits on invalid per spec.
             Computes percent-of-income and routes to a category evaluator in HoweUtil.py.
             Prints formatted results; optionally runs again.
File Created Date: 2026-02-09
Author: Daniel Howe
Version: 1.3
"""

from HoweUtil import (
    evaluate_food,
    evaluate_housing,
    evaluate_savings,
    evaluate_transportation,
)


# ----------------------------
# Variable Initialization Block
# ----------------------------
CATEGORY_OPTIONS = {
    "1": ("Housing", evaluate_housing),
    "2": ("Transportation", evaluate_transportation),
    "3": ("Food", evaluate_food),
    "4": ("Savings", evaluate_savings),
}


def display_category_menu():
    """Print the list of available budget categories."""
    print("\nChoose a budget category:")
    print("1. Housing")
    print("2. Transportation")
    print("3. Food")
    print("4. Savings")


def read_non_empty(prompt_text):
    """Read user input and reject empty values."""
    user_text = input(prompt_text).strip()
    if user_text == "":
        print("Input cannot be empty. Goodbye.")
        return None
    return user_text


def read_positive_number(prompt_text):
    """Read a numeric input and ensure it is greater than zero."""
    raw_value = read_non_empty(prompt_text)
    if raw_value is None:
        return None

    try:
        number = float(raw_value)
    except ValueError:
        print("Input must be numeric. Goodbye.")
        return None

    if number <= 0:
        print("Value must be greater than zero. Goodbye.")
        return None

    return number


def read_category_choice():
    """Read and validate category choice from the menu."""
    display_category_menu()
    choice = read_non_empty("Enter category number (1-4): ")
    if choice is None:
        return None

    if choice not in CATEGORY_OPTIONS:
        print("Invalid category choice. Goodbye.")
        return None

    return choice


def run_once():
    """Execute one complete evaluation cycle. Returns False on invalid input."""
    print("\n--- Monthly Budget Category Evaluator ---")

    monthly_income = read_positive_number("Enter monthly income: $")
    if monthly_income is None:
        return False

    category_choice = read_category_choice()
    if category_choice is None:
        return False

    spending_amount = read_positive_number("Enter amount spent in this category: $")
    if spending_amount is None:
        return False

    if spending_amount > monthly_income:
        print("Spending cannot exceed monthly income. Goodbye.")
        return False

    # Compute percentage and call the evaluator function from the utility module.
    percentage = (spending_amount / monthly_income) * 100
    category_name, evaluator_function = CATEGORY_OPTIONS[category_choice]
    evaluation = evaluator_function(percentage)

    # Display result in a clear, formatted summary block.
    print("\nEvaluation Result")
    print("-" * 40)
    print(f"Income:           ${monthly_income:,.2f}")
    print(f"Category:         {category_name}")
    print(f"Category Spending:${spending_amount:,.2f}")
    print(f"% of Income:      {percentage:.2f}%")
    print(f"Assessment:       {evaluation}")
    print("-" * 40)

    return True


def main():
    """Program entry point with optional repeat loop."""
    continue_running = True

    while continue_running:
        was_successful = run_once()
        if not was_successful:
            break

        run_again = input("\nWould you like to evaluate another category? (y/n): ").strip().lower()
        if run_again != "y":
            continue_running = False

    print("Thank you for using the budget evaluator.")


if __name__ == "__main__":
    main()
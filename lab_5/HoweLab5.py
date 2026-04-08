"""
Project Name: HoweLab5.py
Purpose: Evaluate monthly spending as a percent of income, using loop-controlled input validation
         (max 5 attempts), category evaluators in HoweLab5Util.py, and clear sentence-style output.
Description: Includes income input, category menu choice, spending input, 5-attempt validation loops
             with attempts-remaining feedback, optional quit shortcuts, routing to HoweLab5Util
             evaluators, complete-sentence output, and optional run-again loop.
File Created Date: 2026-02-16
Author: Daniel Howe
Version: 2.1
"""

# ============================================================
# ---- Imports ----
# ============================================================
import sys
import HoweLab5Util

# ============================================================
# ---- Constants (magic numbers / fixed strings) ----
# ============================================================
MAX_ATTEMPTS = 5
QUIT_KEYWORDS = {"q", "quit", "exit"}

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

# ============================================================
# ---- Helper / Utility Functions ----
# ============================================================
def _fail_and_exit(message: str) -> None:
    """
    Print a single error message and terminate the program.

    Exit code policy:
      - sys.exit(1): error termination (rubric: too many invalid attempts / invalid state)
      - sys.exit(0): normal termination (user chooses to quit)
    """
    print(f"ERROR: {message}")
    sys.exit(1)


def _is_quit(s: str) -> bool:
    """Return True if the user input matches a quit keyword."""
    return s.lower() in QUIT_KEYWORDS


# ============================================================
# ---- Input / Validation Functions ----
# ============================================================
def get_valid_income() -> float:
    """
    Prompt for monthly income and validate (max attempts = MAX_ATTEMPTS).

    Returns:
      float: monthly income (> 0)

    Terminates after MAX_ATTEMPTS invalid inputs (empty, non-numeric, <= 0).
    Optional quit: q/quit/exit
    """
    attempts = 0

    def invalid(msg: str) -> None:
        nonlocal attempts
        attempts += 1
        if attempts == MAX_ATTEMPTS:
            _fail_and_exit("Too many invalid attempts. Program terminated.")
        print(msg)
        print(f"Attempts remaining: {MAX_ATTEMPTS - attempts}")

    while attempts < MAX_ATTEMPTS:
        monthly_income_str = input("Enter your monthly income: ").strip()

        # Optional quit shortcut
        if _is_quit(monthly_income_str):
            print("Exiting. Goodbye.")
            sys.exit(0)

        if monthly_income_str == "":
            invalid("Monthly income cannot be empty.")
            continue

        try:
            monthly_income = float(monthly_income_str)
        except ValueError:
            invalid("Monthly income must be numeric.")
            continue

        if monthly_income <= 0:
            invalid("Monthly income must be greater than 0.")
            continue

        return monthly_income

    # Defensive fallback (should be unreachable)
    _fail_and_exit("Too many invalid attempts. Program terminated.")


def get_valid_choice() -> int:
    """
    Prompt for menu choice and validate (max attempts = MAX_ATTEMPTS).

    Returns:
      int: choice (must be a key in MENU_OPTIONS)

    Terminates after MAX_ATTEMPTS invalid inputs (empty, non-integer, not in MENU_OPTIONS).
    Optional quit: q/quit/exit
    """
    attempts = 0

    def invalid(msg: str) -> None:
        nonlocal attempts
        attempts += 1
        if attempts == MAX_ATTEMPTS:
            _fail_and_exit("Too many invalid attempts. Program terminated.")
        print(msg)
        print(f"Attempts remaining: {MAX_ATTEMPTS - attempts}")

    while attempts < MAX_ATTEMPTS:
        choice_str = input("Select a category (enter the number): ").strip()

        # Optional quit shortcut
        if _is_quit(choice_str):
            print("Exiting. Goodbye.")
            sys.exit(0)

        if choice_str == "":
            invalid("Menu choice cannot be empty.")
            continue

        try:
            choice = int(choice_str)
        except ValueError:
            invalid("Menu choice must be an integer.")
            continue

        if choice not in MENU_OPTIONS:
            invalid("Menu choice must be one of the listed options.")
            continue

        return choice

    # Defensive fallback (should be unreachable)
    _fail_and_exit("Too many invalid attempts. Program terminated.")


def get_valid_spending(monthly_income: float, category_label: str) -> float:
    """
    Prompt for category spending and validate (max attempts = MAX_ATTEMPTS).

    Inputs:
      - monthly_income: used to enforce spending <= income (locked policy)
      - category_label: used to personalize the prompt

    Returns:
      float: spending (>= 0 and <= monthly_income)

    Terminates after MAX_ATTEMPTS invalid inputs (empty, non-numeric, < 0, > income).
    Optional quit: q/quit/exit
    """
    attempts = 0

    def invalid(msg: str) -> None:
        nonlocal attempts
        attempts += 1
        if attempts == MAX_ATTEMPTS:
            _fail_and_exit("Too many invalid attempts. Program terminated.")
        print(msg)
        print(f"Attempts remaining: {MAX_ATTEMPTS - attempts}")

    while attempts < MAX_ATTEMPTS:
        spending_str = input(f"Enter your monthly spending for {category_label}: ").strip()

        # Optional quit shortcut
        if _is_quit(spending_str):
            print("Exiting. Goodbye.")
            sys.exit(0)

        if spending_str == "":
            invalid("Spending cannot be empty.")
            continue

        try:
            spending = float(spending_str)
        except ValueError:
            invalid("Spending must be numeric.")
            continue

        if spending < 0:
            invalid("Spending must be 0 or greater.")
            continue

        if spending > monthly_income:
            invalid("Spending cannot exceed monthly income (locked policy).")
            continue

        return spending

    # Defensive fallback (should be unreachable)
    _fail_and_exit("Too many invalid attempts. Program terminated.")


# ============================================================
# ---- Menu Display ----
# ============================================================
def print_menu() -> None:
    """Print the category menu using MENU_OPTIONS."""
    print("\nBudget Categories:")
    for key in sorted(MENU_OPTIONS.keys()):
        print(f"  {key}. {MENU_OPTIONS[key]}")


# ============================================================
# ---- Routing / Processing ----
# ============================================================
def route_evaluation(choice: int, percent_of_income: float) -> str:
    """
    Route to the correct evaluator based on choice.

    Returns:
      str: "Low" | "Typical" | "High"
    """
    # Routing decision: rubric-friendly if/elif
    if choice == 1:
        return HoweLab5Util.evaluate_housing(percent_of_income)
    elif choice == 2:
        return HoweLab5Util.evaluate_food(percent_of_income)
    elif choice == 3:
        return HoweLab5Util.evaluate_transportation(percent_of_income)
    elif choice == 4:
        return HoweLab5Util.evaluate_entertainment(percent_of_income)
    elif choice == 5:
        return HoweLab5Util.evaluate_savings(percent_of_income)

    _fail_and_exit("Unexpected routing state.")


# ============================================================
# ---- Main Program ----
# ============================================================
def main() -> None:
    """Main program flow: inputs → validation → compute → route → output → optional repeat."""
    print("HoweLab5 — Budget Category Evaluator")
    print("Evaluate a category’s monthly spend as a percent of income (Low/Typical/High).")

    # --- Variable Initialization Block (rubric-visible) ---
    monthly_income = 0.0
    choice = 0
    category_label = ""
    spending_amount = 0.0
    percent_of_income = 0.0
    evaluation_result = ""
    run_again = True

    while run_again:
        # --- Input Stage: income ---
        monthly_income = get_valid_income()

        # --- Menu Stage: display + choice ---
        print_menu()
        choice = get_valid_choice()

        # --- Exit Handling ---
        if choice == EXIT_CHOICE:
            print("Exiting. Goodbye.")
            sys.exit(0)

        # --- Input Stage: spending for chosen category ---
        category_label = MENU_OPTIONS[choice]
        spending_amount = get_valid_spending(monthly_income, category_label)

        # --- Compute Stage: percent of income ---
        percent_of_income = spending_amount / monthly_income  # do NOT round before classification

        # --- Route Stage: evaluator selection ---
        evaluation_result = route_evaluation(choice, percent_of_income)

        # --- Output Stage: sentence + report block ---
        print(
            f"Your monthly {category_label} spending of ${spending_amount:,.2f} is "
            f"{percent_of_income * 100:.2f}% of your ${monthly_income:,.2f} income, "
            f"which is considered {evaluation_result}."
        )

        print("\nResult")
        print("-" * 40)
        print(f"Category:          {category_label}")
        print(f"Monthly Income:    ${monthly_income:,.2f}")
        print(f"Category Spend:    ${spending_amount:,.2f}")
        print(f"Percent of Income: {percent_of_income * 100:>10.2f}%")
        print(f"Evaluation:        {evaluation_result}")

        # --- Repeat Stage: run-again prompt ---
        again_str = input("\nRun again? (Y/N): ").strip().lower()
        run_again = again_str in {"y", "yes"}

    print("Done. Goodbye.")


if __name__ == "__main__":
    main()

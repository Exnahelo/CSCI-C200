# Lab 4 Algorithm Design – Budget Category Analyzer

## 1) Problem Description
Create a program that asks the user to enter one numeric value (monthly spending amount)
and select one category from a list of choices (Housing, Food, Transportation, Entertainment,
or Exit). The program validates both inputs. If all inputs are valid, the program analyzes the
spending level and prints whether it is **low**, **moderate**, or **high** for the selected category.

---

## 2) Overall Program Structure

### File A: `budget_category_analyzer.py` (Executable/Main File)
1. File header
2. Import utility function(s) from `budget_utils.py`
3. Create `run_budget_category_analyzer()`
4. Variable initialization block
5. Ask user for spending amount
6. Validate spending amount
   - Check empty input
   - Check numeric format
   - Check non-negative value
7. Display category choices and ask for choice input
8. Validate category choice
   - Must be one of `1`, `2`, `3`, `4`, or `5`
   - If `5`, exit program
9. Call utility module function to analyze spending
10. Display analysis result
11. Run main function using `if __name__ == "__main__":`

### File B: `budget_utils.py` (Utility Module)
1. File header
2. Define one function for each category analysis
   - `analyze_housing(amount)`
   - `analyze_food(amount)`
   - `analyze_transportation(amount)`
   - `analyze_entertainment(amount)`
3. Define dispatcher function `get_analysis_result(choice, amount)`
4. Return appropriate low/moderate/high output text

---

## 3) Detailed Execution Steps (Indented Logic)

1. Start program.
2. Initialize variables.
3. Prompt user: monthly spending amount.
4. If spending input is empty:
   1. Print error message.
   2. End program.
5. Convert spending input to float.
6. If conversion fails:
   1. Print error message.
   2. End program.
7. If spending amount is negative:
   1. Print error message.
   2. End program.
8. Display menu choices (1–5).
9. Prompt user: category choice.
10. If choice is not in valid list:
    1. Print error message.
    2. End program.
11. If choice is `5`:
    1. Print goodbye message.
    2. End program.
12. Send choice + amount to utility module.
13. Utility module selects the correct function.
14. Category function evaluates thresholds and returns low/moderate/high text.
15. Main file prints final sentence:
    - “This spending level is low/moderate/high for this category.”
16. End program.

---

## 4) Utility Function Designs

### `analyze_housing(spending_amount)`
- If amount < 800 → return low
- Else if amount <= 1800 → return moderate
- Else → return high

### `analyze_food(spending_amount)`
- If amount < 250 → return low
- Else if amount <= 700 → return moderate
- Else → return high

### `analyze_transportation(spending_amount)`
- If amount < 150 → return low
- Else if amount <= 500 → return moderate
- Else → return high

### `analyze_entertainment(spending_amount)`
- If amount < 100 → return low
- Else if amount <= 400 → return moderate
- Else → return high

### `get_analysis_result(category_choice, spending_amount)`
- If choice is `1` → call housing function
- If choice is `2` → call food function
- If choice is `3` → call transportation function
- If choice is `4` → call entertainment function
- Else return invalid category (defensive fallback)

---

## 5) Consistency Check (Design vs Program)
- Main actions are in executable file ✅
- Choice-specific logic is grouped in utility file ✅
- Input and choice validations are included ✅
- Program flow follows the algorithm design ✅
budget_category_analyzer.py
budget_category_analyzer.py
New
+81
-0

"""
File: budget_category_analyzer.py
Author: Cash-Flow-Joe Student
Course: Lab 4 - Conditional Executions
Description:
    Executable program that asks the user for a monthly spending amount and a
    budget category choice, validates both inputs, and reports whether the
    spending level is low, moderate, or high for the selected category.
"""

from budget_utils import get_analysis_result


def run_budget_category_analyzer() -> None:
    """Run the interactive budget category analyzer program."""

    # ---------------------------
    # Variable initialization block
    # ---------------------------
    valid_menu_choices = {"1", "2", "3", "4", "5"}
    spending_input = ""
    spending_amount = 0.0
    category_choice = ""

    print("\n=== Budget Category Analyzer ===")
    print("Evaluate spending in different categories.\n")

    # ---------------------------
    # 1) Ask user for spending input
    # ---------------------------
    spending_input = input("Enter your monthly spending amount in dollars: ").strip()

    # ---------------------------
    # 2) Validate spending input
    # ---------------------------
    if spending_input == "":
        print("Input cannot be empty. Goodbye.")
        return

    try:
        spending_amount = float(spending_input)
    except ValueError:
        print("Spending amount must be numeric. Goodbye.")
        return

    if spending_amount < 0:
        print("Spending amount cannot be negative. Goodbye.")
        return

    # ---------------------------
    # 3) Display choice list and ask category input
    # ---------------------------
    print("\nChoose a budget category:")
    print("1. Housing")
    print("2. Food")
    print("3. Transportation")
    print("4. Entertainment")
    print("5. Exit")

    category_choice = input("Enter your choice (1-5): ").strip()

    # ---------------------------
    # 4) Validate category input
    # ---------------------------
    if category_choice not in valid_menu_choices:
        print("Choice must be one of 1, 2, 3, 4, or 5. Goodbye.")
        return

    if category_choice == "5":
        print("You chose to exit. Goodbye.")
        return

    # ---------------------------
    # 5) Perform analysis and display result
    # ---------------------------
    analysis_text = get_analysis_result(category_choice, spending_amount)
    print(f"\nThis spending level is {analysis_text}.")


if __name__ == "__main__":
    run_budget_category_analyzer()
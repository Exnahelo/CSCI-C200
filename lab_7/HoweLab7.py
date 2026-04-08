"""
Project Name: HoweLab7.py
Purpose: Track NASDAQ stock records using parallel arrays.
Description: Menu-driven program for entering, displaying, searching, editing, and deleting stock records with validated input, computed value, and portfolio percentage.
File Created Date: 2026-03-20
Author: Daniel Howe
Version: 1.4
"""

# Maximum number of stock records the program can store.
MAX_SIZE = 100
MIN_INITIAL_ROWS = 4
MAX_SYMBOL_LENGTH = 5
DONE_COMMAND = "done"
CANCEL_COMMAND = "cancel"
EXIT_COMMAND = "exit"


def is_done_command(value):
    """Return True when the user entered the done command."""
    return value.strip().lower() == DONE_COMMAND


def is_cancel_command(value):
    """Return True when the user entered the cancel command."""
    return value.strip().lower() == CANCEL_COMMAND


def is_exit_command(value):
    """Return True when the user entered the exit command."""
    return value.strip().lower() == EXIT_COMMAND


def read_int(prompt, minimum=None):
    """Return a validated integer entered by the user."""
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(
                    f"Please enter a whole number greater than or equal to {minimum}."
                )
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def read_int_or_cancel(prompt, minimum=None):
    """Return a validated integer or cancel if the user aborts entry."""
    while True:
        raw_value = input(prompt).strip()
        if is_cancel_command(raw_value):
            return CANCEL_COMMAND
        try:
            value = int(raw_value)
            if minimum is not None and value < minimum:
                print(
                    f"Please enter a whole number greater than or equal to {minimum}."
                )
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def read_float(prompt, minimum=None):
    """Return a validated floating-point number entered by the user."""
    while True:
        try:
            value = float(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def read_float_or_cancel(prompt, minimum=None):
    """Return a validated float or cancel if the user aborts entry."""
    while True:
        raw_value = input(prompt).strip()
        if is_cancel_command(raw_value):
            return CANCEL_COMMAND
        try:
            value = float(raw_value)
            if minimum is not None and value < minimum:
                print(f"Please enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def find_stock(symbols, count, search_symbol):
    """Return the index of a stock symbol or -1 if it is not found."""
    for index in range(count):
        if symbols[index].upper() == search_symbol.upper():
            return index
    return -1


def validate_stock_symbol(symbol):
    """Return an error message for invalid symbols, or None if valid."""
    if not symbol:
        return "Stock symbol cannot be empty."
    if not symbol.isalpha():
        return "Stock symbol must contain letters only."
    if len(symbol) > MAX_SYMBOL_LENGTH:
        return f"Stock symbol must be {MAX_SYMBOL_LENGTH} letters or fewer."
    return None


def read_stock_symbol(
    symbols,
    count,
    current_index=None,
    allow_done=False,
    allow_cancel=False,
):
    """Read a validated stock symbol and optionally allow done or cancel."""
    while True:
        symbol = input("\nEnter stock symbol: ").strip().upper()

        if allow_done and is_done_command(symbol):
            return DONE_COMMAND

        if allow_cancel and is_cancel_command(symbol):
            return CANCEL_COMMAND

        validation_message = validate_stock_symbol(symbol)
        if validation_message is not None:
            print(validation_message)
            continue

        found_index = find_stock(symbols, count, symbol)
        if found_index not in (-1, current_index):
            print("That stock symbol already exists.")
            continue

        return symbol


def read_search_symbol(prompt):
    """Read a validated stock symbol for a search prompt, or cancel the lookup."""
    while True:
        search_symbol = input(prompt).strip().upper()

        if is_cancel_command(search_symbol):
            return CANCEL_COMMAND

        validation_message = validate_stock_symbol(search_symbol)
        if validation_message is not None:
            print(validation_message)
            continue

        return search_symbol


def display_stocks(symbols, quantities, purchase_prices, count):
    """Display all stock records in a dynamically sized table with totals."""
    if count == 0:
        print("\nNo stocks have been entered.\n")
        return

    total_portfolio_value = 0.0

    for index in range(count):
        total_portfolio_value += quantities[index] * purchase_prices[index]

    headers = ["Symbol", "Qty", "Price", "Value", "%"]
    rows = []

    for index in range(count):
        market_value = quantities[index] * purchase_prices[index]
        portfolio_percentage = 0.0
        if total_portfolio_value > 0:
            portfolio_percentage = (market_value / total_portfolio_value) * 100
        rows.append(
            [
                symbols[index],
                str(quantities[index]),
                f"${purchase_prices[index]:.2f}",
                f"${market_value:.2f}",
                f"{portfolio_percentage:.2f}%",
            ]
        )

    widths = []
    for column_index, header in enumerate(headers):
        column_width = len(header)
        for row in rows:
            column_width = max(column_width, len(row[column_index]))
        widths.append(column_width)

    def format_row(row_values):
        return "  ".join(
            [
                f"{row_values[0]:<{widths[0]}}",
                f"{row_values[1]:>{widths[1]}}",
                f"{row_values[2]:>{widths[2]}}",
                f"{row_values[3]:>{widths[3]}}",
                f"{row_values[4]:>{widths[4]}}",
            ]
        )

    divider = "-" * len(format_row(headers))

    print()
    print(format_row(headers))
    print(divider)
    for row in rows:
        print(format_row(row))
    print(divider)
    total_label = "Total Portfolio Value:"
    total_value = f"${total_portfolio_value:.2f}"
    total_line_width = len(format_row(headers))
    spacing = max(2, total_line_width - len(total_label) - len(total_value))
    print(f"{total_label}{' ' * spacing}{total_value}\n")


def update_stock_symbol(symbols, count, index):
    """Update a stock symbol or cancel the edit."""
    updated_symbol = read_stock_symbol(
        symbols,
        count,
        current_index=index,
        allow_cancel=True,
    )
    if updated_symbol == CANCEL_COMMAND:
        print("Symbol update cancelled.")
        return
    symbols[index] = updated_symbol
    print("Symbol updated.")


def update_stock_quantity(quantities, index):
    """Update a stock quantity or cancel the edit."""
    updated_quantity = read_int_or_cancel("Enter the new quantity: ", minimum=0)
    if updated_quantity == CANCEL_COMMAND:
        print("Quantity update cancelled.")
        return
    quantities[index] = updated_quantity
    print("Quantity updated.")


def update_purchase_price(purchase_prices, index):
    """Update a purchase price or cancel the edit."""
    updated_purchase_price = read_float_or_cancel(
        "Enter the new purchase price: ", minimum=0
    )
    if updated_purchase_price == CANCEL_COMMAND:
        print("Purchase price update cancelled.")
        return
    purchase_prices[index] = updated_purchase_price
    print("Purchase price updated.")


def edit_stock(symbols, quantities, purchase_prices, count, index):
    """Show the edit menu and update fields for the stock at the given index."""
    while True:
        print("\nEdit Menu")
        print("1. Symbol")
        print("2. Quantity")
        print("3. Purchase Price")
        print("4. Return to Main Menu")

        edit_choice = input("Enter your choice: ").strip()

        if edit_choice == "1":
            update_stock_symbol(symbols, count, index)
            continue
        if edit_choice == "2":
            update_stock_quantity(quantities, index)
            continue
        if edit_choice == "3":
            update_purchase_price(purchase_prices, index)
            continue
        if edit_choice == "4":
            break

        print("Invalid choice. Please select 1 through 4.")


def delete_stock(symbols, quantities, purchase_prices, count, found_index):
    """Delete a stock by shifting later records left across all arrays."""
    for index in range(found_index, count - 1):
        symbols[index] = symbols[index + 1]
        quantities[index] = quantities[index + 1]
        purchase_prices[index] = purchase_prices[index + 1]

    symbols[count - 1] = ""
    quantities[count - 1] = 0
    purchase_prices[count - 1] = 0.0

    return count - 1


def collect_stock_record(symbols, count):
    """Collect one complete stock record, or return done/cancel commands."""
    symbol = read_stock_symbol(symbols, count, allow_done=True, allow_cancel=True)

    if symbol == DONE_COMMAND:
        return DONE_COMMAND

    if symbol == CANCEL_COMMAND:
        return CANCEL_COMMAND

    if symbol is None:
        return symbol

    quantity = read_int_or_cancel("Enter quantity: ", minimum=0)
    if quantity == CANCEL_COMMAND:
        return CANCEL_COMMAND

    purchase_price = read_float_or_cancel("Enter purchase price: ", minimum=0)
    if purchase_price == CANCEL_COMMAND:
        return CANCEL_COMMAND

    return symbol, quantity, purchase_price


def add_stock_record(symbols, quantities, purchase_prices, count, stock_record):
    """Store one complete stock record at the same index in all parallel arrays."""
    symbol, quantity, purchase_price = stock_record
    symbols[count] = symbol
    quantities[count] = quantity
    purchase_prices[count] = purchase_price


def collect_initial_data(symbols, quantities, purchase_prices):
    """Collect startup stock data until the user reaches the minimum and enters done."""
    count = 0
    print("NASDAQ Stock Tracker")
    print("Enter at least 4 stocks.")
    print("Type 'done' at the stock symbol prompt to stop.")
    print("Type 'cancel' to abandon the current row.")

    while count < MAX_SIZE:
        stock_record = collect_stock_record(symbols, count)

        if stock_record == DONE_COMMAND:
            if count < MIN_INITIAL_ROWS:
                remaining_rows = MIN_INITIAL_ROWS - count
                print(f"Enter at least {remaining_rows} more stock(s) before stopping.")
                continue
            break

        if stock_record == CANCEL_COMMAND:
            print("Current row cancelled.")
            continue

        if stock_record is None:
            continue

        add_stock_record(symbols, quantities, purchase_prices, count, stock_record)
        count += 1

    if count == MAX_SIZE:
        print("\nMaximum stock capacity reached.")

    return count


def handle_edit(symbols, quantities, purchase_prices, count):
    """Search for a stock and start the edit workflow if it is found."""
    if count == 0:
        print("No stocks are available to edit.")
        return

    search_symbol = read_search_symbol("Edit symbol ('cancel' to return): ")
    if search_symbol == CANCEL_COMMAND:
        print("Edit cancelled.")
        return

    found_index = find_stock(symbols, count, search_symbol)

    if found_index == -1:
        print("Stock not found.")
        return

    edit_stock(symbols, quantities, purchase_prices, count, found_index)


def handle_add(symbols, quantities, purchase_prices, count):
    """Collect and add one new stock record from the main menu."""
    if count >= MAX_SIZE:
        print("Maximum stock capacity reached.")
        return count

    stock_record = collect_stock_record(symbols, count)

    if stock_record == DONE_COMMAND:
        print("Use 'exit' from the main menu to end the program.")
        return count

    if stock_record == CANCEL_COMMAND:
        print("Add stock cancelled.")
        return count

    if stock_record is None:
        return count

    add_stock_record(symbols, quantities, purchase_prices, count, stock_record)
    print(f"{stock_record[0]} was added.")
    return count + 1


def handle_delete(symbols, quantities, purchase_prices, count):
    """Search for a stock and delete it when the minimum row rule allows it."""
    if count == 0:
        print("No stocks are available to delete.")
        return count

    if count <= MIN_INITIAL_ROWS:
        print(
            f"At least {MIN_INITIAL_ROWS} stocks are required. Delete is unavailable."
        )
        return count

    search_symbol = read_search_symbol("Delete symbol ('cancel' to return): ")
    if search_symbol == CANCEL_COMMAND:
        print("Delete cancelled.")
        return count

    found_index = find_stock(symbols, count, search_symbol)

    if found_index == -1:
        print("Stock not found.")
        return count

    deleted_symbol = symbols[found_index]
    count = delete_stock(
        symbols,
        quantities,
        purchase_prices,
        count,
        found_index,
    )
    print(f"{deleted_symbol} was deleted.")
    return count


def run_menu(symbols, quantities, purchase_prices, count):
    """Display the portfolio and run the main menu loop until exit."""
    while True:
        display_stocks(symbols, quantities, purchase_prices, count)
        print("Main Menu")
        print("1. Add a stock")
        print("2. Edit a stock")
        print("3. Delete a stock")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            count = handle_add(symbols, quantities, purchase_prices, count)
        elif choice == "2":
            handle_edit(symbols, quantities, purchase_prices, count)
        elif choice == "3":
            count = handle_delete(symbols, quantities, purchase_prices, count)
        elif choice == "4" or is_exit_command(choice):
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1 through 4.")


def main():
    """Create the stock arrays, collect data, and start the menu loop."""
    # These are parallel 1-D arrays where each shared index represents one stock record.
    symbols = [""] * MAX_SIZE
    quantities = [0] * MAX_SIZE
    purchase_prices = [0.0] * MAX_SIZE

    count = collect_initial_data(symbols, quantities, purchase_prices)

    run_menu(symbols, quantities, purchase_prices, count)


if __name__ == "__main__":
    main()

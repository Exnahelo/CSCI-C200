"""
Project Name: HoweLab6.py
Purpose: Parse a finance symbol in the format TICKER-EXCHANGE using required string indexing
         and slicing (without split()), returning the ticker and exchange in sentence-style output.
Description: Includes a user input loop for entering symbols in the required format, a run-again
             prompt for unlimited attempts, a string-processing function that locates the separator
             index and slices the input into ticker and exchange parts, and complete-sentence output
             showing the original input and extracted components.
File Created Date: 2026-02-23
Author: Daniel Howe
Version: 1.0
"""

# ============================================================
# ---- Constants ----
# ============================================================
SEPARATOR = "-"


# ============================================================
# ---- String Processing Function (required) ----
# ============================================================
def parseSymbol(symbol: str) -> tuple[str, str]:
    """
    Parse a symbol in the form TICKER-EXCHANGE into (ticker, exchange) using indexing/slicing.
    Rules:
      - Find the first '-' (first separator wins).
      - Left side is ticker, right side is exchange.
      - Strip whitespace around each part; preserve original letter case.
    Note: No validation required by blueprint; if '-' is missing, exchange will be "".
    """
    dash_index = symbol.find(SEPARATOR)

    # If no dash is found, keep ticker as the whole string and exchange as empty.
    if dash_index == -1:
        ticker = symbol.strip()
        exchange = ""
        return ticker, exchange

    ticker = symbol[:dash_index].strip()
    exchange = symbol[dash_index + 1 :].strip()
    return ticker, exchange


# ============================================================
# ---- Main Program ----
# ============================================================
def main() -> None:
    """Main loop: input → parseSymbol() → output → run-again decision."""
    print(
        "Welcome to Lab 6: Enter a symbol like TICKER-EXCHANGE and I’ll parse it into ticker + exchange."
    )

    continue_choice = "yes"  # loop control default

    while continue_choice.strip().lower() != "no":
        symbol = input("Enter a symbol in format TICKER-EXCHANGE (example: AAPL-NASDAQ): ").strip()

        ticker, exchange = parseSymbol(symbol)

        print(
            f"In the symbol '{symbol}', '{ticker}' is the ticker and '{exchange}' is the exchange."
        )

        continue_choice = input("Try another symbol? Type yes to continue or no to quit: ")

    print("Done. Goodbye.")


if __name__ == "__main__":
    main()

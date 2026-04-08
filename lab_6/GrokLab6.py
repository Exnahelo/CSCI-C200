def main():
    continue_program = True
    while continue_program:
        # Ask the user to enter a stock symbol
        stock_symbol = input(
            "Enter a stock symbol in the format TICKER-EXCHANGE (e.g., AAPL-NASDAQ): "
        )

        # Find the position of the hyphen
        hyphen_index = stock_symbol.find("-")

        # Extract the ticker and exchange using slicing
        ticker = stock_symbol[:hyphen_index]
        exchange = stock_symbol[hyphen_index + 1 :]

        # Print the formatted sentence
        print(f"The ticker is {ticker} and the exchange is {exchange}.")

        # Ask if the user wants to continue
        user_choice = input(
            "Do you want to enter another stock symbol? (y/n): "
        ).lower()
        if user_choice != "y":
            continue_program = False


if __name__ == "__main__":
    main()

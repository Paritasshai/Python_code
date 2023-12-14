def StockPicker(prices):
    if len(prices) < 2:
        return -1  # There must be at least two prices to make a profit

    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        # Update the minimum price if a lower price is found
        min_price = min(min_price, price)
    if max_profit == 0:
        return -1  # No chance to make a profit

        # Update the maximum profit if a better selling opportunity is found
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Example usage with user input:
user_stock_prices = input("Enter the stock prices separated by spaces: ")
stock_prices = list(map(int, user_stock_prices.split()))

result = StockPicker(stock_prices)
print(result)
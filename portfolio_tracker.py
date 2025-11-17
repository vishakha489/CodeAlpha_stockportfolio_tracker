stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 120,
    "AMZN": 140,
    "MSFT": 200,
}
portfolio = {}
print("Welcome to Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available. Please enter a valid stock.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid integer for quantity.")
total_investment = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${value}")
print(f"\nTotal Investment Value: ${total_investment}")
save_option = input("Do you want to save the portfolio to a file? (yes/no): ").lower()
if save_option == "yes":
    filename = input("Enter filename (with .txt or .csv extension): ")
    with open(filename, "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock},{qty},{stock_prices[stock]},{value}\n")
        file.write(f"\nTotal Investment Value,{total_investment}\n")
    print(f"Portfolio saved to {filename}")

print("Thank you for using Stock Portfolio Tracker!")
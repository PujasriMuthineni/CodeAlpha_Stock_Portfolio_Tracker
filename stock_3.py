# Stock Portfolio Tracker - Single Program

import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130
}

total_investment = 0
portfolio = []

n = int(input("Enter number of different stocks: "))

for i in range(n):
    stock = input("Enter stock name (AAPL/TSLA/GOOGL/AMZN): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value
        portfolio.append([stock, quantity, price, value])
        print(f"{stock} investment value: ${value}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Save to text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for item in portfolio:
        file.write(f"{item[0]} - Qty: {item[1]}, Price: ${item[2]}, Value: ${item[3]}\n")
    file.write(f"\nTotal Investment Value: ${total_investment}")

# Save to CSV file
with open("portfolio.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Value"])
    writer.writerows(portfolio)
    writer.writerow(["Total", "", "", total_investment])

print("Portfolio saved to portfolio.txt and portfolio.csv")
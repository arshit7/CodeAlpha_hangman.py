stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 200
}

total = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        value = stocks[stock] * quantity
        total += value
        print(f"Value of {stock}: ₹{value}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value = ₹", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ₹{total}")

print("Portfolio saved to portfolio.txt")
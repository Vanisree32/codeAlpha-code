stocks = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 140,
    "MICROSoFT": 330
}

total_value = 0

print("=== STOCK PORTFOLIO TRACKER ===")

while True:

    stock = input(
        "Enter Stock Name (or 'done' to finish): "
    ).upper()

    if stock == "DONE":
        break

    if stock not in stocks:
        print("Stock not available!")
        continue

    try:

        quantity = int(
            input("Enter Quantity: ")
        )

        if quantity <= 0:
            print(
                "Quantity must be greater than 0"
            )
            continue

        investment = (
            stocks[stock] * quantity
        )

        total_value += investment

        print(
            f"{stock} Investment Value = ${investment}"
        )

    except ValueError:
        print(
            "Please enter valid quantity"
        )

print(
    "\nTotal Portfolio Value = $",
    total_value
)

with open(
    "portfolio.txt",
    "w"
) as file:

    file.write(
        f"Total Portfolio Value = ${total_value}"
    )

print(
    "Portfolio saved to portfolio.txt"
)

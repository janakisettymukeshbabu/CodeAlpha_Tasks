# Stock Portfolio Tracker – CodeAlpha Internship
# Author: Janakisetty Mukesh Babu

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOG": 1350,
    "AMZN": 1500,
    "TCS": 3900,
    "INFY": 1450,
}

portfolio = []


def add_stock():
    print("\nAdd a Stock")
    name = input("Enter stock name: ").strip().upper()

    if name not in STOCK_PRICES:
        print("Price not available for this stock. Try another.")
        return

    qty_in = input("Enter quantity: ").strip()
    if not qty_in.isdigit():
        print("Invalid quantity.")
        return

    qty = int(qty_in)
    price = STOCK_PRICES[name]
    value = price * qty

    entry = {"name": name, "qty": qty, "price": price, "value": value}
    portfolio.append(entry)

    print(f"Added: {name} ({qty} shares @ {price})")


def view_portfolio():
    print("\nPortfolio Summary")

    if not portfolio:
        print("No entries yet.")
        return

    print(f"{'Stock':<8}{'Qty':<8}{'Price':<12}{'Value'}")
    for row in portfolio:
        print(f"{row['name']:<8}{row['qty']:<8}{row['price']:<12}{row['value']}")


def total_value():
    if not portfolio:
        print("\nPortfolio empty.")
        return

    t = sum(x["value"] for x in portfolio)
    print("\nTotal Investment Value:", t)


def save_report():
    if not portfolio:
        print("\nNothing to save.")
        return

    with open("portfolio_report.txt", "w") as f:
        f.write("Stock Portfolio Report\n\n")
        for row in portfolio:
            f.write(f"{row['name']}  Qty:{row['qty']}  Price:{row['price']}  Value:{row['value']}\n")
        f.write("\nTotal Value: " + str(sum(x["value"] for x in portfolio)))

    print("Saved as portfolio_report.txt")


def menu():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Total Value")
        print("4. Save Report")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_stock()
        elif choice == "2":
            view_portfolio()
        elif choice == "3":
            total_value()
        elif choice == "4":
            save_report()
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()

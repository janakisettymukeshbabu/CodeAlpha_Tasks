# 📊 Stock Portfolio Tracker — CodeAlpha Internship

This is a Python-based Stock Portfolio Tracker built for the **CodeAlpha Python Programming Internship**.  
The program calculates the total portfolio value using **predefined stock prices** (as required by the task).

---

## ✨ Features

- Add stocks using:
  - Stock symbol  
  - Quantity  
- Uses predefined prices (dictionary-based)
- Calculates values:
  - Value per stock = qty × price  
  - Total portfolio value  
- View portfolio in table format
- Export portfolio summary to `portfolio_report.txt`
- 100% offline (no internet required)

---

## 🧠 How It Works

The script maintains:

```
portfolio = [
    {"name": "AAPL", "qty": 2, "price": 180, "value": 360},
    ...
]
```

Price lookup is performed using a fixed dictionary:

```
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "GOOG": 1350,
    "AMZN": 1500,
    "TCS": 3900,
    "INFY": 1450,
}
```

The user interacts through a simple menu:

1. Add Stock  
2. View Portfolio  
3. Show Total Value  
4. Save Report  
5. Exit  

---

## ▶️ How to Run

```
python stocktracker.py
```

Example usage:

```
Enter stock name: AAPL
Enter quantity: 5
→ Added: AAPL (5 shares @ 180)
```

---

## 📁 Project Info

- **Internship:** CodeAlpha – Python Programming  
- **Task:** Stock Portfolio Tracker  
- **Developer:** Janakisetty Mukesh Babu

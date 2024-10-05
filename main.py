# library
import random
import time
from threading import Thread

# from local files
from market import update_stock_prices
from trading import buy_stock, sell_stock, calculate_profit_loss

# initial data
stocks = {
    "stockA": 100.0,
    "stockB": 50.0,
    "stockC": 25.0
}
users = {
    "user1": {"balance": 1000, "stocks": {}},
    "user2": {"balance": 2000, "stocks": {}}
}

# start the real-time stock price updates in a separate thread
Thread(target=lambda: update_stock_prices(stocks), daemon=True).start()

def display_info():
    print("\n------------------------------")
    print("Current stock prices:", {s: f"{p:.2f}" for s, p in stocks.items()})
    
    for user in users:
        profit_loss = calculate_profit_loss(users, stocks, user)
        print(f"{user}: Profit/Loss = {profit_loss:.2f}")
        # Stop Loss
        if profit_loss < -100:
            print(f"notice: {user} has reached the Stop Loss!!!")

# Program loop
while True:
    display_info()
    
    action = input("Input (buy/sell/refresh/quit): ").lower()
    if action == "quit" or action == "q":
        break
    elif action == "refresh" or action == "r":
        print("refreshing ...")
        time.sleep(1)
        continue
    elif action in ["buy", "sell"]:
        user = input("user: ")
        stock = input("stocks: ")
        quantity = int(input("quantity: "))
        
        if action == "buy":
            result = buy_stock(users, stocks, user, stock, quantity)
        else:
            result = sell_stock(users, stocks, user, stock, quantity)
        print(result)
    else:
        print("Invalid command. Please try again.")
    
    time.sleep(1)

print("\n------------------------------")
print("exiting ...")
print("have a nice day!")
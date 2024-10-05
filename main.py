# library
import time
from threading import Thread

# from local files
from market import update_stock_prices
from trading import buy_stock, sell_stock, calculate_profit_loss, set_take_profit, set_stop_loss, check_take_profit_stop_loss

# initial data
stocks = {
    "stockA": 100.0,
    "stockB": 50.0,
    "stockC": 25.0
}
users = {
    "user1": {"balance": 1000, "stocks": {}, "take_profit": 0, "stop_loss": 0},
    "user2": {"balance": 2000, "stocks": {}, "take_profit": 0, "stop_loss": 0}
}

# start the real-time stock price updates in a separate thread
Thread(target=lambda: update_stock_prices(stocks), daemon=True).start()

def display_info():
    print("\n------------------------------------------------------------------------------------------")
    print("Current stock prices:", {s: f"{p:.2f}" for s, p in stocks.items()})
    print("------------------------------------------------------------------------------------------")
    
    for user in users:
        profit_loss = calculate_profit_loss(users, stocks, user)
        
        print(f"{user}: Profit/Loss = {profit_loss:.2f}")
        print("balance:", users[user]["balance"])
        print("stocks:", users[user]["stocks"])
        print(f"Take Profit: {users[user]['take_profit']}, Stop Loss: {users[user]['stop_loss']}\n")

# Program loop
while True:
    display_info()
    check_take_profit_stop_loss(users, stocks)
    
    print("------------------------------")
    print("commands: buy | sell | refresh | take profit | stop loss | quit")
    
    action = input("Input: ").lower()
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
    elif action == "take profit":
        user = input("user: ")
        profit = float(input("take profit: "))
        result = set_take_profit(users, user, profit)
        print(result)
    elif action == "stop loss":
        user = input("user: ")
        loss = float(input("stop loss: "))
        result = set_stop_loss(users, user, -abs(loss))  # Make sure it's negative
        print(result)
    else:
        print("Invalid command. Please try again.")
    
    time.sleep(1)

print("\n------------------------------")
print("exiting ...")
print("have a nice day!")
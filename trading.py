# buy
def buy_stock(users, stocks, user, stock, quantity):
    if stock not in stocks:
        return "no this stock in market"
    
    cost = stocks[stock] * quantity
    if users[user]["balance"] < cost:
        return "Not enough money"
    
    users[user]["balance"] -= cost
    users[user]["stocks"][stock] = users[user]["stocks"].get(stock, 0) + quantity
    return f"order: buy {quantity} {stock} at {stocks[stock]:.2f} bath"

# sell
def sell_stock(users, stocks, user, stock, quantity):
    if stock not in users[user]["stocks"] or users[user]["stocks"][stock] < quantity:
        return "stock is not enough"
    
    monney = stocks[stock] * quantity
    users[user]["balance"] += monney
    users[user]["stocks"][stock] -= quantity
    if users[user]["stocks"][stock] == 0:
        del users[user]["stocks"][stock]
    return f"order: sell {quantity} {stock} at {stocks[stock]:.2f} bath"

# calculate profit/loss
def calculate_profit_loss(users, stocks, user):
    current_balance = users[user]["balance"]
    stock_value = 0
    for stock, quantity in users[user]["stocks"].items():
        stock_value += stocks[stock] * quantity
    total_value = current_balance + stock_value
    return total_value - (1000 if user == "user1" else 2000)

# set take profit
def set_take_profit(users, user, profit):
    users[user]["take_profit"] = profit
    return f"Take profit set to {profit} for {user}"

# set stop loss
def set_stop_loss(users, user, loss):
    users[user]["stop_loss"] = loss
    return f"Stop loss set to {loss} for {user}"

# check and execute take profit or stop loss
def check_take_profit_stop_loss(users, stocks):
    for user in users:
        profit_loss = calculate_profit_loss(users, stocks, user)
        if users[user]["take_profit"] > 0 and profit_loss >= users[user]["take_profit"]:
            sell_all_stocks(users, stocks, user)
            print(f"Take profit executed for {user}. All stocks sold.")
            users[user]["take_profit"] = 0
        elif users[user]["stop_loss"] < 0 and profit_loss <= users[user]["stop_loss"]:
            sell_all_stocks(users, stocks, user)
            print(f"Stop loss executed for {user}. All stocks sold.")
            users[user]["stop_loss"] = 0

# sell all stocks for a user
def sell_all_stocks(users, stocks, user):
    for stock, quantity in list(users[user]["stocks"].items()):
        sell_stock(users, stocks, user, stock, quantity)
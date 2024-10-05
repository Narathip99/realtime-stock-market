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
    
    profit = stocks[stock] * quantity
    users[user]["balance"] += profit
    users[user]["stocks"][stock] -= quantity
    return f"order: sell {quantity} {stock} at {stocks[stock]:.2f} bath"

# calculate profit/loss
def calculate_profit_loss(users, stocks, user):
    initial_balance = 1000 if user == "user1" else 2000
    current_balance = users[user]["balance"]
    for stock, quantity in users[user]["stocks"].items():
        current_balance += stocks[stock] * quantity
    return current_balance - initial_balance
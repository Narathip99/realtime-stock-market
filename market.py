# library
import random
import time

# Update stock prices by a random percentage every second
def update_stock_prices(stocks):
    while True:
        for stock in stocks:
            change = random.uniform(-1, 1)
            stocks[stock] *= (1 + change / 100) 
        time.sleep(1)
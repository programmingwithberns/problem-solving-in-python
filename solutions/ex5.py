""" 
You are interested in buying crypto-currencies. 
You want to check the current amount of money you have 
and see how many coins you can buy in Bitcoin, Ethereum,
and Litecoin.

Create a program that:
1. Reads the total amount of money you have
2. Reads the price of Bitcoin, Ethereum, and Litecoin
3. Prints the amount of Bitcoin, Ethereum, and Litecoin you can buy
Example: money = 100, bitcoin_price = 50, ethereum_price = 25, litecoin_price = 10
Output: "With 100$ you can buy: 2 Bitcoins, 4 Ethereum, and 10 Litecoins"
"""
from utils import get_float, get_integer

# read the money
money = get_integer("How much money do you have ?(Whole numbers): ", 100, 1000000)

bitcoin_price = get_float("Enter price of BTC: ", 1, 100000)

ethereum_price = get_float("Enter the price of ETH: ", 1, 4000)

litecoin_price = get_float("Enter the price of LTC: ", 1, 300)

btc_amount = money / bitcoin_price

eth_amount = money / ethereum_price 

ltc_amount = money / litecoin_price

print(f"\nGiven an amount of ${money}, you can purchase ", end="")

print(f"{round(btc_amount,2)} BTC or {round(eth_amount, 2)} ETH or {ltc_amount} LTC.")

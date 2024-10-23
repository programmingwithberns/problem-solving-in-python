"""
You are interested in buying a new laptop. You check the price and you see that the price is 300$ without the 10% tax.
Create a program that:
1. Reads the price of the laptop
2. Reads the tax percentage
3. Prints the total amount
Output: "The total price of the laptop is 330$
"""
# input
from utils import get_float

price = get_float("Please enter the price of the laptop: ", 0, 10000)

tax_percent = get_float("Please enter the tax percent: ",0, 35)

# processing 
vat = (tax_percent / 100) * price 

total_cost = price + vat

print(f"Price of laptop is ${price} and vat is ${vat}. The total price is ${total_cost}")
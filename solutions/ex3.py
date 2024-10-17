""" 
You've bought a Bitcoin and now it's on the rise!!!
 
Create a program that:
1) Reads the value of the bitcoin at the time of purchase
2) Reads the percentage of increase (or decrease)
3) Prints the total value of your bitcoin
4) Prints the increase or decrease value

* Example: bitcoin_value = 10000, bitcoin_increase = 10
* Output: total_bitcoin_value = 11000, bitcoin_increase_value = 1000
"""
# input
btc_value = float(input("Please enter the current value of BTC: "))

percent_increase = float(input("Please enter the percentage increase: "))

# processing 
increase_value = btc_value * (percent_increase / 100)

total_btc_value = btc_value  + increase_value 

# print out the output
print(f"For a purchace price of ${btc_value} of BTC, the increase of {percent_increase} ({percent_increase/100})", end="")
print(f"Current value of BTC after {percent_increase} % increase is {total_btc_value}")

print(f"The BTC increase value is {increase_value}")
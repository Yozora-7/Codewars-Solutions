"""
Task:
Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accept 1 parameters:n, n is the number of customers to buy hotdogs, different numbers have different prices (refer to the following table), return a number that the customer need to pay how much money.

number	price (cents)
n < 5	100
n >= 5 and n < 10	95
n >= 10	90
You can use if..else or ternary operator to complete it.
"""

def sale_hotdogs(n):
    if n < 5:
        return 100 * n
    elif n >= 5 and n < 10:
        return 95 * n
    elif n >= 10:
        return 90 * n
      
# another example

def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)

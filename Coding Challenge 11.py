# Coding Challenge 11
# Consider a list in Python which includes prices of all the items in a store.
# Build a function to discount the price of all the products by 10%.
# Use map to apply the function to all the elements of the list so that all the product prices are discounted.

store = [100, 200, 300]
def disc():
    shop = list(map(lambda x: x - (x * 10) / 100, store)) #Pass list as an argument - map(function, iterables)
    print(shop)
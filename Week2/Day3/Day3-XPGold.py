# Exercise 4: Fruit Shop

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# 1.Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
for item, price in items.items():
    print(f"{item.capitalize()}'s price is {str(price)}.")
print("\n")

# 2.Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
# write some code to calculate how much it would cost to buy everything in stock.
items = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

for item, info in items.items():
    total_price = info['price'] * info['stock']
    print(f"{item.capitalize()}'s total price is {str(total_price)}.")

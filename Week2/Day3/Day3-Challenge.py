# Challenge 1
#     Ask a user for a word
#     Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
#         Make sure the letters are the keys.
#         Make sure the letters are strings.
#         Make sure the indexes are stored in a list and those lists are values.

user_input = input("Enter a word: ")
letter_indexs = {}
for i, letter in enumerate(user_input):
    if letter not in letter_indexs:
        letter_indexs[letter] = [i]
    else:
        letter_indexs[letter].append(i)
print(letter_indexs)

# --------------------------------------------------
# Challenge 2
#     Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
#     Sort the list in alphabetical order.
#     Return “Nothing” if you can’t afford anything from the store.

# Scenario 1: price is in string with "$"
items_purchase = {
    "Phone": "$999",
    "Speakers": "$300",
    "Laptop": "$5,000",
    "PC": "$1200"
}

# assume user input is number
wallet_input = int(input("Money in your wallet: $"))
afford_list = []
for key, value in items_purchase.items():
    # for $1,000 we need to remove $ and ',' to compare the price
    item_price = int(value.split("$")[-1].replace(',', ''))
    if wallet_input >= item_price:
        afford_list.append(key)
# check if the list is empty
if not afford_list:
    print("Nothing")
else:
    print(sorted(afford_list))

# Scenario 2: items_purchase list is from user-input
# assume user input format as "water:1 bread:3 tv:1000 fertilizer:20"
item_input = input("Please put item and price: ")
item_dict = {item.split(":")[0]: int(item.split(":")[-1]) for item in item_input.split(" ")}
wallet_input = int(input("Money in your wallet: $"))
afford_list = []
for key, value in item_dict.items():
    if wallet_input >= value:
        afford_list.append(key.capitalize())
# check if the list is empty
if not afford_list:
    print("Nothing")
else:
    print(sorted(afford_list))

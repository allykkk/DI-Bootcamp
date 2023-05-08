# 🌟 Exercise 1 : Set
my_fav_numbers = {2, 7, 8, 9}
my_fav_numbers.update([15, 17])
# print(my_fav_numbers)
my_fav_numbers.remove(7)
# print(my_fav_numbers)
friend_fav_numbers = {5, 9, 17, 21, 28}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# --------------------------------------------------------------------
# 🌟 Exercise 2: Tuple
thistuple = ("apple", "banana", "cherry")
# A tuple is a collection which is ordered and unchangeable.

# --------------------------------------------------------------------
# 🌟 Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
# print(basket)
basket.count("Apples")
basket.clear()
print(basket)

# --------------------------------------------------------------------
# 🌟 Exercise 4: Floats
my_list = []
for i in range(1, 5):
    my_list.append(i + 0.5)
    my_list.append(i + 1)
print(my_list)


# --------------------------------------------------------------------
# 🌟 Exercise 5: For Loop
for i in range(1, 21):
    print(i)
    # Solution No.1
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
    # Solution No.2
for i in range(2, 21, 2):
    print(i)

# --------------------------------------------------------------------
# 🌟 Exercise 6 : While Loop
my_name = "ally"
user_input = ""
while user_input.lower() != my_name:
    user_input = input("Please enter your name: ")

# --------------------------------------------------------------------
# 🌟 Exercise 7: Favorite Fruits
user7_input_list=input('Please type your favourite fruits. Please separate the fruits with a single space, eg. "apple mango cherry" : ').lower()
user7_fruit_list=user7_input_list.split(" ")
# print(user7_fruit_list)
user7_input_fruit=input("input a name of any fruit:")
if user7_input_fruit.lower() in user7_fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# --------------------------------------------------------------------
# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

topping_list = []
while True:
    user_input = input("Please enter a series of pizza toppings (or 'quit' to finish): ").lower()
    if user_input == "quit":
        break
    else:
        print(f"Adding '{user_input}' to your pizza.")
        topping_list.append(user_input)

topping_count = len(topping_list)
pizza_price = 10 + 2.5 * topping_count

if topping_count > 0:
    toppings_str = ", ".join(topping_list)
    print(f"You added {topping_count} topping{'s' if topping_count > 1 else ''}: {toppings_str}")
else:
    print("You didn't add any toppings.")

print(f"The total price is {pizza_price} dollars.")


# --------------------------------------------------------------------
# Exercise 9: Cinemax
# Instructions
# 1. A movie theater charges different ticket prices depending on a person’s age.
#     if a person is under the age of 3, the ticket is free.
#     if they are between 3 and 12, the ticket is $10.
#     if they are over the age of 12, the ticket is $15.
#
# 2. Ask a family the age of each person who wants a ticket.
#
# 3. Store the total cost of all the family’s tickets and print it out.

total_price = 0
while True:
    user_age = input("please type your age if you want to purchase the ticket ('q' for quitting'): ")
    if user_age.lower() == "q":
        print(f"Total price is: {total_price}")
        break
    try:
        # string "2.7" can not be converted to int directly
        age = int(float(user_age))
        if age in range (3,13):
            total_price += 10
        if age >= 13:
            total_price += 15
    except ValueError:
        print("please type a number!!")

# 4. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.


name_list=['Mike', 'Will','Nancy','Lucas','Max']
approved_name=[]
for name in name_list:
# While True loop is for the edge case - invalid input, eg: non int input  will jump to error message and skip age question.
    while True:
        namelist_age=input(f"Hey {name}, Please type your age: ")
        try:
            teen_age=int(namelist_age)
            if teen_age<16 or teen_age>21:
                print("Sorry, you are restricted to watch the movie.")
                break
            else:
                approved_name.append(name)
                break
        except ValueError:
            print("Please type your age with number !")
print(" ".join(approved_name))

# --------------------------------------------------------------------
# Exercise 10 : Sandwich Orders

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
for order in sandwich_orders:
    finished_sandwiches.append(order)
    print(f"I made your {order}")
    print("\n")

# --------------------------------------------------------------------
# Exercise 11 : Sandwich Orders 2
sandwich_orders2 = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich",
                    "Pastrami sandwich", "Pastrami sandwich"]
finished_sandwiches2 = []
failed_order = []
print("Sorry, the deli has run out of pastrami.")
while "Pastrami sandwich" in sandwich_orders2:
    sandwich_orders2.remove("Pastrami sandwich")
for order in sandwich_orders2:
    finished_sandwiches2.append(order)
    print(f"I made your {order}")

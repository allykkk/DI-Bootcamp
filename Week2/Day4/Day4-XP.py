import random


# Exercise 1 : What are you learning ?


# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.
def display_message():
    print("I am learning python.")


display_message()


# ------------------------------------------------------
# 🌟 Exercise 2: What’s your favorite book ?

# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
def favorite_book(title):
    print(f"One of my favorite book is {title.capitalize()}.")


favorite_book("alice in Wonderland")


# ------------------------------------------------------
# 🌟 Exercise 3: Some Geography

# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# Give the country parameter a default value.
def describe_city(city, country='Iceland'):
    print(f"{city.capitalize()} is in {country.capitalize()}.")


describe_city("reykjavik")


# ------------------------------------------------------
# 🌟 Exercise 4 : Random

# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
def compare_with_random(number):
    random_num = random.randint(1, 100)
    if number > 100 or number < 1:
        print("Please enter number between 1 and 100!!")
    else:
        if number == random_num:
            print("Congrats! Your number is the same as random number!")
        else:
            print(f"You have failed! The number you entered is : {number}. The random number is : {random_num}.")


num_input = int(input("Please eneter a random number between 1 and 100: "))
compare_with_random(num_input)


# ------------------------------------------------------
# 🌟 Exercise 5 : Let’s create some personalized shirts !

# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
def make_shirt(size="large", message="I love Python"):
    print(f'The size of the shirt is <{size}> and the text is "{message}".')


# Make a large shirt with the default message
make_shirt()
# Make medium shirt with the default message
make_shirt("medium")
# Make a shirt of any size with a different message.
make_shirt("s", "hello world")
# Call the function make_shirt() using keyword arguments.
make_shirt(message="Keep calm and code Python")


# ------------------------------------------------------
# 🌟 Exercise 6 : Magicians

def show_magicians(magician_list):
    for item in magician_list:
        print(item, end=" ; ")
    print("\n")


# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
def make_great(magician_list):
    for i in range(0, len(magician_list)):
        magician_list[i] = "the Great " + magician_list[i]


# Using this list of magician’s names.
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
show_magicians(magician_names)
# Call the function make_great().
make_great(magician_names)
# Call the function show_magicians() to see that the list has actually been modified.
show_magicians(magician_names)


# ------------------------------------------------------
# 🌟 Exercise 7 : Temperature Advice

# Create a function called get_random_temp().
# def get_random_temp():
#     return random.randint(-10, 40)

def get_random_temp(season):
    if season == 'winter':
        lower_limit = -10
        upper_limit = 16
    elif season == 'spring':
        lower_limit = 0
        upper_limit = 23
    elif season == 'summer':
        lower_limit = 24
        upper_limit = 32
    elif season == 'fall':
        lower_limit = 16
        upper_limit = 24
    else:
        raise ValueError('Invalid season')

    return random.randint(lower_limit, upper_limit)


def convert_season():
    # assume perfect input, only int
    month = int(input("Please type a month: "))
    if month in [12, 1, 2]:
        # Winter (Dec, Jan, Feb)
        return "winter"
    elif month in [3, 4, 5]:
        # Spring (Mar, Apr, May)
        return "spring"
    elif month in [6, 7, 8]:
        # Summer (Jun, Jul, Aug)
        return "summer"
    elif month in [9, 10, 11]:
        # Fall (Sep, Oct, Nov)
        return "fall"
    else:
        # Invalid month number
        print("Invalid month number entered!")
        return None


# Create a function called main().
def main():
    # Inform the user in a friendly message
    season = convert_season()
    print(season)
    random_temp = get_random_temp(season)
    print(random_temp)
    # print(f"The temperature right now is {random_temp} degrees Celsius.")
    if random_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 16 > random_temp >= 0:
        print("Quite chilly! Don’t forget your coat")
    elif 23 > random_temp >= 16:
        print("It's a bit cool out today. You might want to bring a light jacket.")
    elif 32 > random_temp >= 23:
        print("It's a comfortable temperature today. Enjoy the nice weather!")
    elif 40 > random_temp >= 32:
        print("It's getting pretty warm out there. Make sure to stay hydrated and wear sunscreen.")


# Test your function to make sure it generates expected results.
# print(get_random_temp())
main()

# 🌟 Exercise 1 : Convert lists into dictionaries
# Instructions:
#     Convert the two following lists, into dictionaries.
#     Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

# ----------------------------------------------------
# 🌟 Exercise 2 : Cinemax
# Instructions
#     A movie theater charges different ticket prices depending on a person’s age.
#         if a person is under the age of 3, the ticket is free.
#         if they are between 3 and 12, the ticket is $10.
#         if they are over the age of 12, the ticket is $15.
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_price = 0
for name in family.keys():
    if 12 >= family[name] >= 3:
        total_price += 10
    elif family[name] > 12:
        total_price += 15
print(f"Total cost for the family is ${total_price}.")

# bonus - method one
# assume user put all at once, eg: rick 43 beth 13 morty 5 summer 8
user_input = input("Please put name and age for your family member:")
name_age_list = user_input.split(" ")
dict = {}
for i in range(0, len(name_age_list), 2):
    dict[name_age_list[i]] = int(name_age_list[i + 1])
print(dict)

# bonus - method two
user_input = input("Please put name and age for your family member:")
name_age_list = user_input.split(" ")
# name_list=name_age_list[0::2]
# name_age_list=name_age_list[1::2]
name_age_dict = {name: int(age) for name, age in zip(name_age_list[::2], name_age_list[1::2])}
print(name_age_dict)

# ----------------------------------------------------
# 🌟 Exercise 3: Zara
# 1. Here is some information about a brand.
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {"name": "Zara",
         "creation_date": 1975,
         "creator_name": "Amancio Ortega Gaona",
         "type_of_clothes": ["men", "women", "children", "home"],
         "international_competitors": ["Gap", "H&M", "Benetton"],
         "number_stores": 7000,
         "major_color": {" France": "blue", "Spain": "red", "US": ["pink", "green"]}
         }

# 3. Change the number of stores to 2.
brand['number_stores'] = 2

# 4. Print a sentence that explains who Zaras clients are.
print(f"{brand['name']}'s clients include women and men, mainly younger adults in the age range of 18 to 40.")

# 5. Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'Spain'

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if 'Desigual' not in brand['international_competitors']:
    brand['international_competitors'].append('Desigual')

    # 7. Delete the information about the date of creation.
del brand['creation_date']
print(brand)

# 8. Print the last international competitor.
print(brand['international_competitors'][-1])

# 9. Print the major clothes colors in the US.
print(f"Major clothes colors in the US are {' and '.join(brand['major_color']['US'])}.")

# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

# 11. Print the keys of the dictionary.
for key in brand.keys():
    print(key, end=" ; ")

    # 12. Create another dictionary called more_on_zara with the following details:
more_on_zara = {'creation_date': 1975, 'number_stores': 10000}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
print(brand)

# 14. Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])

# ----------------------------------------------------
# 🌟 Exercise 4 : Disney characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# 1.Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
# ----------------------------------

# dict1 = {}
# for i in range(0, 5):
#     dict1[users[i]] = i
dict1 = {user: i for i, user in enumerate(users)}
print(dict1)

# 2.Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
# ----------------------------------

# dict2 = {}
# for i in range(0, 5):
#     dict2[i] = users[i]
dict2 = {i: user for i, user in enumerate(users)}
print(dict2)

# 3.Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# ----------------------------------

# dict3 = {}
# for i in range(0, 5):
#     dict3[sorted(users)[i]] = i
dict3 = {user: i for i, user in enumerate(sorted(users))}
print(dict3)

# 4.Only recreate the 1st result for:
#     The characters, which names contain the letter “i”.
#     The characters, which names start with the letter “m” or “p”.
# ----------------------------------

filtered_list = []
dict4 = {}
for user in users:
    if (user[0].lower() in ['m', 'p']) or (user.find("i") != -1):
        filtered_list.append(user)
# print(filtered_list)

dict4 = {user: i for i, user in enumerate(filtered_list)}
print(dict4)

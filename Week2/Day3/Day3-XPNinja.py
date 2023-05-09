# Exercise 1 : Cars
# --------------------------------

# 1.Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
given_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# 2.Convert it into a list using Python (don’t do it by hand!).
companies_list = given_string.split(", ")

# 3.Print out a message saying how many manufacturers/companies are in the list.
print(f"There are {len(companies_list)} companies in the list.")

# 4.Print the list of manufacturers in reverse/descending order (Z-A)
companies_list.sort(reverse=True)
print(companies_list)  # companies_list=['Volkswagen', 'Toyota', 'Honda', 'Ford Motor', 'Chevrolet']

# 5.Using loops or list comprehension:

#     Find out how many manufacturers’ names do not have the letter ‘i’ in them.
#     Find out how many manufacturers’ names have the letter ‘o’ in them.
o_count = len([company for company in companies_list if "o" in company])
without_i_count = len([company for company in companies_list if "i" not in company])

# 6.Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
duplicate_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
#     Remove these programmatically. (Hint: you can use set to help you).
clean_set = set(duplicate_list)
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.
print(f"Companies list is: {', '.join(clean_set)}.")
print(f"There are {str(len(clean_set))} companies in the list.")

# 7.Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.
companies_list.sort()
reversed_letter_list = [company[::-1] for company in companies_list]
print(reversed_letter_list)

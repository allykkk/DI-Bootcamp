# Exercise 4 : How Many Characters In A Sentence ?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam, quis nostrud exercitation ullamcolaboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velitesse cillum dolore eu fugiat nulla pariatur.Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

# Exercise 5: Longest Word Without A Specific Character
max_length = 0
max_attempts = 5
for i in range(max_attempts):
    user_input = input("Try to make a longest sentence without the character 'A' : ")
    if "a" in user_input.lower():
        print('You typed "A"!')
    else:
        if len(user_input) > max_length:
            print("you have made a longest sentence with " + str(len(user_input)) + " letters!")
            max_length = len(user_input)
        else:
            print("You have failed to make a longer sentence!")

    if i == max_attempts - 1:
        print("The end!")

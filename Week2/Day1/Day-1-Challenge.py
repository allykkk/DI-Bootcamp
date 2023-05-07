import random

x = input("Please put something 10 characters long: ")
strip_x = x.replace(" ", "")
if len(strip_x) < 10:
    print("string not long enough")
if len(strip_x) > 10:
    print("string too long")
else:
    print("Your first letter is " + x[0] + " ,Your last letter is " + x[-1])
    loop_print = ""
    for letter in x:
        loop_print += letter
        print(loop_print)
    list_input = [letter for letter in strip_x]
    random.shuffle(list_input)
    print("".join(list_input))

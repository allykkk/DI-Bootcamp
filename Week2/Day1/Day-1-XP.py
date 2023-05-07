# 🌟 Exercise 1 : Hello World
print("Hello Word\n" * 4)


# 🌟 Exercise 2 : Some Math
print((99 ^ 3) * 8)
print("\n")


# 🌟 Exercise 3 : What Is The Output ?
print(5 < 3)
print(3 == 3)
print(3 == '3')
# print("3">3) -- TypeError
print(bool("Hello" == "hello"))
print("\n")


# 🌟 Exercise 4 : Your Computer Brand
computer_brand = "Lenovo"
print("I have a " + computer_brand + " computer")
print("\n")


# 🌟 Exercise 5 : Your Information
name = "Ally"
age = 25
shoe_size = 37
# info = "My name is " + name + ". I am " + str(age) + " years old." + " My shoe size is " + str(shoe_size) + ".\n"
info=f"My name is {name}. I am {str(age)} years old. My shoe size is {str(shoe_size)}. "
print(info)


# 🌟 Exercise 6 : A & B
a = 5
b = 3
if a > b:
    print("Hello World.\n")


# 🌟 Exercise 7 : Odd Or Even
while True:
    x = input("Please type a number: ")
    try:
        if int(x) % 2 == 0:
            print(x + " is an even number.")
        elif int(x) % 2 != 0:
            print(x + " is an odd number.")
        break
    except ValueError:
        print("Number only, please!")


# 🌟 Exercise 8 : What’s Your Name ?
x = input("What is your name? ")
if x == "Ally" or x == "ally":
    print("Hey, we have the same name!")
else:
    print("Do you want to reconsider your name?")


# 🌟 Exercise 9 : Tall Enough To Ride A Roller Coaster
    # converting from cms to inches
    """ 1 inch = 2.54 centimeters """
x = int(input("Please write your height in inches: ")) * 2.54
if x < 145:
    print(" You are not tall enough to ride it.")
    # John Rogan as the tallest person -- he was measured by doctors at 8 ft 11.1 in (2.72 m).
elif 145 <= x <= 272:
    print("Congrats! You are tall enough to ride it.")
else:
    print("Please type in inches!!!")

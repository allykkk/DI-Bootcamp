# Exercise 1 : Hello World-I Love Python
print("Hello world\n" * 4 + "I love Python\n" * 4)

# Exercise 2 : What Is The Season ?
while True:
    x = input("Please input a month: ")
    try:
        if int(x) not in range(1, 13):
            print("Please type number from 1 to 12!")
        else:
            if int(x) in range(3, 6):
                print("Spring")
            elif int(x) in range(6, 9):
                print("Summer")
            elif int(x) in range(9, 12):
                print("Autumn")
            elif int(x) in [12, 1, 2]:
                print("Winter")
            break
    except ValueError:
        print("Please type NUMBER from 1 to 12!")



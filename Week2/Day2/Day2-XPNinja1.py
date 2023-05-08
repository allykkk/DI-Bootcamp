import math


def get_number(user_input):
    num_list = []
    for i in user_input.split(","):
        num_list.append(int(i))
    return num_list


def formula(D):
    C = 50
    H = 30
    Q = math.sqrt((2 * C * D) / H)
    return int(Q)


user_input = input("Please type a few numbers: ")
for i in get_number(user_input):
    print(formula(i))

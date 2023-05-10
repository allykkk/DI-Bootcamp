from functools import reduce
import random


# Exercise 2 : Sum
def x_sum(num):
    # return value as X+XX+XXX+XXXX
    add_list = list(map(lambda i: i * str(num), range(1, 5)))
    total_sum = reduce(lambda x, y: int(x) + int(y), add_list)
    return total_sum


print(x_sum(3))


# ----------------------------------------------------------------
# Exercise 3 : Double Dice
def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    doubles_list = [(throw_dice(), throw_dice())]
    while doubles_list[-1][0] != doubles_list[-1][1]:
        doubles_list.append((throw_dice(), throw_dice()))
    # print(doubles_list)
    return len(doubles_list)


def main():
    count_list = [throw_until_doubles() for i in range(100)]
    # After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
    print(f"The total throw number is : {sum(count_list)}.")
    # print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
    average_count = sum(count_list) / len(count_list)
    print(f"The total average throw number is : {round(average_count, 2)}")
    return None


# print(throw_until_doubles())
main()

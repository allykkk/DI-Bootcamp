# Challenge1
def create_list():
    list = []
    number = int(input("Please type a number: "))
    length = int(input("Please define the length of your list: "))
    for i in range(0, length):
        list.append(number * (i + 1))
    return list


# Challenge2
def remove_duplicates(word):
    result = ""
    prev_char = ""
    for char in word:
        if char != prev_char:
            result += char
        prev_char = char
    return result


# chanllenge 1
print(create_list())

# chanllenge 2
user_input = input("Please type a word: ")
print(remove_duplicates(user_input))




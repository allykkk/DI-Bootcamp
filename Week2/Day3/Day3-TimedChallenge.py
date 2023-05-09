# Timed Challenge #1
# Write a program to reverse the sentence wordwise.
#
# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You

word_list = input("please type a sentence : ").split(" ")
reversed_sentence = " ".join(word_list[::-1])
print(reversed_sentence)

# -------------------------------------------------
# Timed Challenge #2
# find perfect numbers
number_input = int(input("Please enter a number: "))  # assume user input is perfect. Only number, not letters.
division_sum = 0
for i in range(1, number_input):
    if number_input % i == 0:
        division_sum += i
if division_sum == number_input:
    print("Perfect number.")
else:
    print("Not a perfect number.")

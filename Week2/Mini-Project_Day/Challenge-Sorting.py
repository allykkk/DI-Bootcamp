def word_sort(input:str):
    print(",".join(sorted(input.split(","))))

user_input="without,hello,bag,world,hello"
word_sort(user_input)
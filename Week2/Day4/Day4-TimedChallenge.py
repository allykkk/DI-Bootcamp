# Timed Challenge #1

# Assume perfect input - string
def count_occurence(sentence: str, letter: str) -> int:
    return sentence.lower().count(letter.lower())


sentence = input("Please type a sentence: ")
letter = input("Please type a letter: ")
print(count_occurence(sentence, letter))



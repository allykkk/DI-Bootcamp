# instruction: Create a new file called anagram_checker.py which contains a class called AnagramChecker
class AnagramChecker:
    # instruction: __init__ - should load the word list file (text file) into a variable.
    def __init__(self):
        with open('sowpods.txt', 'r') as file:
            self.valid_word_list = file.read().splitlines()

    # instruction: is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.
    def is_valid_word(self, word):
        # all words in the file are in big letters
        return True if word.upper() in self.valid_word_list else False

    # instruction: get_anagrams(word) – should find all anagrams for the given word.
    def get_anagrams(self, word: str):
        user_word_list = sorted(list(word.upper()))
        anagrams = []
        for valid_word in self.valid_word_list:
            if sorted(list(valid_word)) == user_word_list and word.upper() != valid_word:
                anagrams.append(valid_word)
        return anagrams

# test = AnagramChecker()
# print(test.get_anagrams("meat"))
# print(test.is_valid_word("meat"))

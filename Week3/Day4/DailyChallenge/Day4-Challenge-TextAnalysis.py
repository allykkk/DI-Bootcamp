# The goal of the exercise is to create a class that will help you analyze a specific text.
# A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.

import string, re, nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


class Text():
    def __init__(self, text: str):
        self.text = text

    # instruction: Implement a classmethod that returns a Text instance but with a text file.
    @classmethod
    def read_file(cls, filename):
        with open(filename, 'r', encoding='utf-8', errors='replace') as file:
            text = file.read()
        return cls(text)

    #  instruction: creates a method to return the frequency of a word in the text, return None or a meaningful message.
    def frequency_analysis(self):
        if not self.text:
            return None
        # first create a dict with each word as key, frequency as value
        frequency_dict_word = {}
        # replace . to prevent the last word from being categorized as a new word
        text_list = self.text.replace(".", "").split(" ")
        for word in text_list:
            frequency_dict_word[word] = frequency_dict_word.get(word, 0) + 1
        frequency_dict_number = {}
        # create a more useful dict with frequency as key, words in list as value
        for k, v in frequency_dict_word.items():
            frequency_dict_number.setdefault(v, []).append(k)
        return frequency_dict_number

    # instruction: creates a method that returns the most common word in the text.
    def most_common_word(self):
        frequency_dict = self.frequency_analysis()
        most_common_words = frequency_dict[max(frequency_dict)]
        word_text = "word is" if len(most_common_words) == 1 else "words are"
        common_words_text = ' ; '.join(most_common_words)
        print(f"The most common {word_text}: {common_words_text}")

    # instruction: creates a method that returns a list of all the unique words in the text.
    def unique_words(self):
        # it is a simple task, not calling the frequency_analysis() function to save running time
        text_list = self.text.replace(".", "").split(" ")
        unique_words = set()
        # to prevent from having word like '\nmother' in the returned list
        for word in text_list:
            word = word.strip()  # Strip leading/trailing whitespace
            if word:  # Check if word is not empty after stripping whitespace
                unique_words.add(word)
        return list(unique_words)


# instruction: Create a class called TextModification that inherits from Text.
class TextModification(Text):
    def __init__(self, text: str):
        super().__init__(text)

    # instruction: creates a method that returns the text without any punctuation.
    def remove_punctuation(self):
        translation_table = str.maketrans("", "", string.punctuation)
        no_punctuation = self.text.translate(translation_table)
        return no_punctuation

    # instruction: creates a method that returns the text without any english stop-words.
    def remove_stopwords(self):
        stop_words = set(stopwords.words('english'))
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        no_stopwords = ' '.join(filtered_words)
        return no_stopwords

    # instruction: creates a method that returns the text without any special characters.
    def remove_special_characters(self):
        no_special_chars = re.sub(r'[^a-zA-Z0-9\s]', '', self.text)
        return no_special_chars


# text = "A good book would sometimes cost as much as a good house."
# ob = Text(text)
# print(ob.frequency_analysis())
# ob.most_common_word()
# print(ob.unique_words())
file = Text.read_file("the_stranger.txt")
file.most_common_word()
# print(file.unique_words())
text = "Hello, world! This is an example text."
modified_text = TextModification(text)
print(modified_text.remove_punctuation())
print(modified_text.remove_stopwords())
print(modified_text.remove_special_characters())

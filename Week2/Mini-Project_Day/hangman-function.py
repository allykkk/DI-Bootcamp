import random


def choose_word():
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
                 'credit card', 'rush', 'south']
    word = random.choice(wordslist)
    hidden_word_list = ['#' if char != ' ' else ' ' for char in word]
    return word, hidden_word_list


def create_letter_dict(word):
    letter_dict = {}
    for index, letter in enumerate(word):
        if letter not in letter_dict:
            letter_dict[letter] = [index]
        else:
            letter_dict[letter].append(index)
    return letter_dict


def play_game(guessing_obj):
    body_part = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
    word, hidden_word_list = guessing_obj
    print("".join(hidden_word_list))
    letter_dict = create_letter_dict(word)

    while body_part:
        user_input = input("Guess a letter: ")
        if user_input not in word:
            print(f"{body_part.pop()} has been added to the gallows. You have {len(body_part)} chances left!")
        else:
            for index in letter_dict[user_input]:
                hidden_word_list[index] = user_input
                if ("".join(hidden_word_list)) == word:
                    print(f"Congrats! The word is <{word}> !")
                    body_part = False
            print("".join(hidden_word_list))


guessing_obj = choose_word()
play_game(guessing_obj)

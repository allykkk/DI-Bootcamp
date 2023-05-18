from anagram_checker import AnagramChecker


def display_menu():
    # Y for enter the game, Q for quiting the game
    print("Welcome to Anagram Checker!\n")
    print("* Enter the program: Y")
    print("* Exit the program: Any other word")


def input_check():
    while True:
        print("**********************************************************************")
        # instruction: Whitespace should be removed from the start and end of the user’s input.
        word_input = input("YOUR WORD : ").strip()
        # instruction: Show a menu, offering the user to input a word or exit.
        # Keep showing the menu until the user chooses to exit.
        if word_input.lower() == "q":
            print("************************ Program Exited! *****************************")
            return None
        # instruction: Only a single word is allowed. If the user typed more than one word, show an error message.
        elif " " in word_input:
            print("Please enter only a single word.")
        # instruction: Only alphabetic characters are allowed. No numbers or special characters.
        elif not word_input.isalpha():
            print("Please enter only alphabetic characters.")
        else:
            return word_input


def anagram_check(word_input):
    # instruction: Display the information about the word in a user-friendly, nicely-formatted message.
    anagram_checker = AnagramChecker()
    if anagram_checker.is_valid_word(word_input):
        print("This is a valid English word.")
        anagrams_result = anagram_checker.get_anagrams(word_input)
        if anagrams_result:
            print(f"Anagrams for your word: {', '.join(anagrams_result)}")
        else:
            print("No anagrams found for your word.")
    else:
        print("This is not a valid English word.")
    print("**********************************************************************\n")


def main():
    display_menu()
    menu_choice = input("\nPlease enter: ")
    print("\n")
    # only "y" will start the program, other keys will exit the program.
    if menu_choice.upper() == "Y":
        while True:
            # check if user input is a single English word or if user wants to quit the program.
            word_input = input_check()
            # exit the program if user type "q"
            if word_input is None: return None
            # user checker to give relevant result
            anagram_check(word_input)
            print("Do you want to check another word?")
            restart = input("Y to continue, else quit the program:  ")
            print("\n")
            # restart the program to check the next word
            if restart.lower() == 'y':
                continue
            else:
                print("************************ Program Exited! *****************************")
                return None
    else:
        print("************************ Program Exited! *****************************")


main()

# instruction: this file/module should contain a class called Game. It should have 4 methods
import random


class Game:
    valid_list = ['r', 'p', 's']
    winning_combinations = [('r', 's'), ('p', 'r'), ('s', 'p')]

    # instruction: get_user_item(self) – ask the user to select an item (rock/paper/scissors).
    def get_user_item(self):
        # instruction: Keep asking until the user has selected one of the items
        while True:
            user_selection = input("Select (r)rock, (p)paper, or (s)scissors: ")
            if user_selection.lower() in self.valid_list:
                # instruction: Return the item at the end of the function.
                return user_selection
            else:
                print("Please choose from r, p, s! Try again!")

    # instruction: get_computer_item(self) – Select rock/paper/scissors at random for the computer.
    def get_computer_item(self):
        computer_selection = random.choice(self.valid_list)
        return computer_selection

    # instruction: get_game_result(self, user_item, computer_item) – Determine the result of the game.
    # instruction: Return either win, draw, or loss.
    def get_game_result(self, user_item, computer_item):
        game_combination = (user_item, computer_item)
        if game_combination in self.winning_combinations:
            return "win"
        elif user_item == computer_item:
            return "draw"
        else:
            return "lose"

    # instruction: play(self) – the function that will be called from outside the class .
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        # instruction: Print the output of the game like : “You selected rock. The computer selected paper. You lose”
        print(f"You selected {user_item}. The computer selected {computer_item}. You {result}.\n")
        return result

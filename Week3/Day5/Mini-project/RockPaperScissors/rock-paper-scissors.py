from game import Game


def get_user_menu_choice():
    print("*****************************************************")
    print("Menu:")
    print("(g) Play a new game")
    print("(x) Show scores and exit")
    user_choice = input(" :")
    print("*****************************************************\n")
    return user_choice


def print_results(results: dict):
    print("Game Results:")
    for result, count in results.items():
        print(f"    * You {result} {count} times")
    print("\nThank you for playing!")


def main():
    game_results = {}
    is_continue = True
    while is_continue:
        user_choice = get_user_menu_choice()
        if user_choice.lower() not in ['x', 'g']:
            print("Wrong input, please try again!")
            continue
        elif user_choice == 'g':
            game = Game()
            result = game.play()
            game_results[result] = game_results.get(result, 0) + 1
            continue
        else:  # user_choice == 'x':
            is_continue = False
            if not game_results:
                print(" You haven't tried the game!")
            else:
                print_results(game_results)


main()


row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

game_board = [row1, row2, row3]


def display_board():
    print("TIC TAC TOE")
    print("*" * 17)
    print(f"*   {row1[0]} | {row1[1]} | {row1[2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {row2[0]} | {row2[1]} | {row2[2]}   *")
    print("*  ---|---|---  *")
    print(f"*   {row3[0]} | {row3[1]} | {row3[2]}   *")
    print("*" * 17)


# make sure user input is 1,2,3,and not used
def input_validation(prompt):
    while True:
        try:
            number = int(input(prompt)) - 1
            if 0 <= number <= 2:
                return number
            print("Don't think out side of the box now !!!!")
        except Exception:
            print("Not a number!!!")
            continue


def player_input(user_name):
    print(f"Player {user_name} 's turn...\n")
    # assume input only number
    # user input -1 converts to list index standard
    while True:
        row_index = input_validation("Enter row: ")
        col_index = input_validation("Enter column: ")
        if game_board[row_index][col_index] == " ":
            game_board[row_index][col_index] = user_name
            return row_index, col_index
        else:
            print("Wait, that's illegal!")


def check_win(user_input_list):
    winning_diag_one = [(0, 0), (1, 1), (2, 2)]
    winning_diag_two = [(0, 2), (1, 1), (2, 0)]
    # check if 3 marks are reached in row or column
    user_row_list = [coordinate[0] for coordinate in user_input_list]
    user_column_list = [coordinate[1] for coordinate in user_input_list]

    # Check rows / columns
    for i in range(3):
        count_row = user_row_list.count(i)
        count_column = user_column_list.count(i)
        # check if 3 marks are reached in rows or columns
        if count_row == 3 or count_column == 3:
            return True

    # Check diagonals
    if all(item in user_input_list for item in winning_diag_one) or all(
            item in user_input_list for item in winning_diag_two):
        return True

    return False


def process_player_turn(user_name, user_input_list):
    user_row, user_column = player_input(user_name)
    display_board()
    user_input_list.append((user_row, user_column))
    if check_win(user_input_list):
        print(f"{user_name} Won!")
        return True
    return False


def play():
    print('Welcome to TIC TAC TOE!\n')
    x_input_list = []
    o_input_list = []
    display_board()

    for i in range(9):
        if i % 2 == 0:
            if process_player_turn("X", x_input_list): break
        else:
            if process_player_turn("O", o_input_list): break

        if i == 8:
            print("Even")


play()

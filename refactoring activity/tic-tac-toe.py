import os

def clear_screen():
    # clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def show(board):
    # print the board
    for row_idx in range(3):
        print(f" {board[row_idx * 3]} | {board[row_idx * 3 + 1]} | {board[row_idx * 3 + 2]} ")
        if row_idx < 2:
            print("---+---+---")

# return 'X' or 'O' if there's a winner, otherwise None.
def winner(board):
    # list of all winning combinations
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c]:
            return board[a]  # Return 'X' or 'O'

    return None  # No winner yet

def play():
    board = [str(i) for i in range(9)]
    player = 'X'

    while any(cell.isdigit() for cell in board):
        clear_screen()
        print("Tic-Tac-Toe\n")
        show(board)
        print(f"\n{player}'s turn!")

        try:
            move = int(input("Pick a spot (0-8): "))
        except ValueError:
            print("Invalid input. Please enter a number from 0 to 8.")
            continue

        if 0 <= move < 9 and board[move].isdigit():
            board[move] = player

            if winner(board):
                clear_screen()
                show(board)
                print(f"\n{player} wins!")
                return

            # Switch players
            player = 'O' if player == 'X' else 'X'
        else:
            print("That spot is taken or out of range. Try again.")

    clear_screen()
    print("Tic-Tac-Toe\n")
    show(board)
    print("\nIt's a draw!")

play()

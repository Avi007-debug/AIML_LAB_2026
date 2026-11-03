def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def dfs(board, player):
    # Check terminal states
    if check_winner(board, 'X'):
        return 1

    if check_winner(board, 'O'):
        return -1

    if is_board_full(board):
        return 0

    scores = []

    # Try every possible empty position
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':

                board[i][j] = player

                # Recursively explore the next state
                score = dfs(board, 'O' if player == 'X' else 'X')

                # Backtracking:
                # Undo the move after exploring it
                board[i][j] = ' '

                scores.append(score)

    # X = AI → maximize score
    # O = Human → minimize score
    if player == 'X':
        return max(scores)
    else:
        return min(scores)


def find_best_move(board):
    best_score = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':

                # Try an X move
                board[i][j] = 'X'

                # After X moves, O gets the turn
                score = dfs(board, 'O')

                # Undo the move
                board[i][j] = ' '

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            print("AI is making a move...")

            row, col = find_best_move(board)
            board[row][col] = 'X'

        else:
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))

                    if 0 <= row <= 2 and 0 <= col <= 2:
                        if board[row][col] == ' ':
                            board[row][col] = 'O'
                            break
                        else:
                            print("Cell already occupied. Try again.")
                    else:
                        print("Enter values between 0 and 2.")

                except ValueError:
                    print("Invalid input. Enter numbers between 0 and 2.")

        # Check whether the current player won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'


play_game()
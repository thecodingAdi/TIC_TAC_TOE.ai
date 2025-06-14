import math


HUMAN = 'O'
AI = 'X'
EMPTY = ' '

 
board = [EMPTY] * 9

 
def print_board():
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print('| ' + ' | '.join(row) + ' |')

 
def check_winner(b, player):
    win_states = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    return any(all(b[i] == player for i in line) for line in win_states)

def is_draw(b):
    return all(cell != EMPTY for cell in b)
 
def minimax(b, depth, is_max, alpha, beta):
    if check_winner(b, AI):
        return 10 - depth
    if check_winner(b, HUMAN):
        return depth - 10
    if is_draw(b):
        return 0

    if is_max:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == EMPTY:
                b[i] = AI
                eval = minimax(b, depth + 1, False, alpha, beta)
                b[i] = EMPTY
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == EMPTY:
                b[i] = HUMAN
                eval = minimax(b, depth + 1, True, alpha, beta)
                b[i] = EMPTY
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

 
def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = AI

 
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == EMPTY:
                board[move] = HUMAN
                break
            else:
                print("That spot is taken!")
        except:
            print("Invalid input. Enter a number from 1 to 9.")
 
def play_game():
    print("You are 'O'. AI is 'X'.")
    print_board()
    while True:
        human_move()
        print_board()
        if check_winner(board, HUMAN):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if check_winner(board, AI):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

 
if __name__ == "__main__":
    play_game()

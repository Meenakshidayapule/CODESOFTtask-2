def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def evaluate(board):
    # Check rows for victory
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return 10 if row[0] == 'X' else -10

    # Check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 10 if board[0][2] == 'X' else -10

    return 0

def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)
    
    if score == 10:
        return score - depth
    
    if score == -10:
        return score + depth
    
    if not is_moves_left(board):
        return 0
    
    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = ' '
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max, alpha, beta))
                    board[i][j] = ' '
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False, -1000, 1000)
                board[i][j] = ' '
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_turn = True
    
    while True:
        print_board(board)
        
        if evaluate(board) == 10:
            print("AI wins!")
            break
        elif evaluate(board) == -10:
            print("Human wins!")
            break
        elif not is_moves_left(board):
            print("It's a tie!")
            break
        
        if human_turn:
            move = input("Enter your move (row and column): ").split()
            row, col = int(move[0]), int(move[1])
            if board[row][col] == ' ':
                board[row][col] = 'O'
                human_turn = False
        else:
            row, col = find_best_move(board)
            board[row][col] = 'X'
            human_turn = True

play_game()
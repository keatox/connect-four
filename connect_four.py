from random import randint

def print_board(board):
    #prints board based on given dimensions
    header = ' '
    for num in range(1, len(board)+1):
        header += ' '+ str(num) +'  '
    print(header)
    print('\u250C'+'---\u252C' * (len(board)-1) +'---\u2510')

    for row in range(len(board[0])):
        print('|   ' * (len(board) +1))
        row_with_items = ''
        for col in range(len(board)):
            row_with_items += ('| '+str(board[col][row])) + ' '
        print(row_with_items + '|')
        print('|   ' * (len(board) +1))
        if row != len(board[0])-1:
            print('\u251C---' + '\u253C---' * (len(board)-1) + '\u2524')
        else:
            print('\u2514---' + '\u2534---' * (len(board)-1) + '\u2518')

def valid_move(board, move):
	# returns False if move is outside of board dimensions
    if move < 1 or move > (len(board)):
        return False
    # returns False if the column is full
    if board[move-1][0] != ' ':
        return False
    return True

def select_space(board, col, player):
	# checks for valid move
    if not valid_move(board, col):
        print("Trying to place an " + player + " in column " + str(col))
        print("Pick a column between 1 and " + str(len(board)) + " that is not full")
        print()
        return False

    # places piece in given column
    for square in range(len(board[0])-1, -1, -1):
        if board[col-1][square] == ' ':
            board[col-1][square] = player
            print("Placed an " + player + " in column " + str(col))
            print()
            return True
    return False

def available_moves(board):
    # returns available columns 
    moves = []
    for i in range(1, len(board)+1):
        if valid_move(board, i):
            moves.append(i)
    return moves

def win(board, symbol):
    # check horizontal spaces
    for y in range(len(board[0])):
        for x in range(len(board) - 3):
            if board[x][y] == symbol and board[x+1][y] == symbol and board[x+2][y] == symbol and board[x+3][y] == symbol:
                return True

    # check vertical spaces
    for x in range(len(board)):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x][y+1] == symbol and board[x][y+2] == symbol and board[x][y+3] == symbol:
                return True

    # check diagonal spaces
    for x in range(len(board) - 3):
        for y in range(3, len(board[0])):
            if board[x][y] == symbol and board[x+1][y-1] == symbol and board[x+2][y-2] == symbol and board[x+3][y-3] == symbol:
                return True
    for x in range(len(board) - 3):
        for y in range(len(board[0]) - 3):
            if board[x][y] == symbol and board[x+1][y+1] == symbol and board[x+2][y+2] == symbol and board[x+3][y+3] == symbol:
                return True
    return False

def game_is_over(board):
  # returns True if game is won or no moves are left
  return win(board, "X") or win(board, "O") or len(available_moves(board)) == 0

def play():
    # sets board dimensions
    my_board = []
    for col in range(7):
        my_board.append([' '] * 6)
    multi = input("Would you like to play singleplayer or multiplayer? Select S/M accordingly.")
    #runs game
    if multi.lower() == 'm':
        turn = "O"
        winner = False
        while(not game_is_over(my_board)):
            print_board(my_board)
            move = 0
            available = available_moves(my_board)
            while (move not in available):
                move = int(input("It is " + turn + "'s turn. Please select a column. Your optionns are " + str(available)))
            select_space(my_board, move, turn)

            if win(my_board, turn):
                print(turn + " has won!")
                print_board(my_board)
                winner = True
                break

            if turn == 'O':
                turn = "X"
            else:
                turn = 'O'
                
        if not winner:
            print("It was a tie!")
            print_board(my_board)

play()
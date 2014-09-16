import random

def displayBoard(board):
    # The Tic Tac Toe board

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] +' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] +' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] +' | '+board[3])
    print('   |   |')
    print('-----------')
    

def getPlayerInput():
    # get Player Input, which letter Player want to use to play Tic Tac.
    letter = '';
    while not (letter=='X' or letter=='O'):
        print('Do you want letter X or O?')
        letter = raw_input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoFirst():
    if random.randint(0, 1) == 0:
        return 'Computer'
    else:
        return 'Player'

def isWinner(board, le):
    return ((board[1] == le and board[2]==le and board[3]==le) or
            (board[4] == le and board[5]==le and board[6]==le) or
            (board[7] == le and board[8]==le and board[9]==le) or
            (board[7] == le and board[4]==le and board[1]==le) or
            (board[8] == le and board[5]==le and board[2]==le) or
            (board[9] == le and board[6]==le and board[3]==le) or
            (board[7] == le and board[5]==le and board[3]==le) or
            (board[9] == le and board[5]==le and board[1]==le))

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getplayerMove(board):
    # get player move details
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next Move? (1-9)')
        move = raw_input()
    return int(move)

def makeMove(board, letter, move):
    board[move] = letter


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(board, computerLetter):
                return i
    # Check if player can win and place computer letter there

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
             makeMove(copy, playerLetter, i)
             if isWinner(copy, playerLetter):
                 return i
     # Check if any of the corner is free
    move = chooseRandomMoveFromList(board, playerLetter, [1, 3, 7, 9])
    if move != None:
        return move
    # Check if Center of board is free
    if isSpaceFree(board, 5):
        return 5

    # check move on one of the side
    return chooseRandomMoveFromList(board, playerLetter, [2, 4, 6, 8])
# modified this method to add more AI to Computer
def chooseRandomMoveFromList(board, playerLetter, movesList):       
    possibleWinMoves = []
    possibleMoves = []
    canPlayerWin = False
    for i in movesList:
        copy = getBoardCopy(board)
        if isSpaceFree(board, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                possibleWinMoves.append(i)
                canPlayerWin = True
            else:
                possibleMoves.append(i)


    if len(possibleWinMoves) != 0 and canPlayerWin:
        return random.choice(possibleWinMoves)
    else:
        if len(possibleMoves)!=0:
            return random.choice(possibleMoves)
        else:
            return None

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('WELCOME TO TIC-TAC-TOE!..')

while True:
    #Reset the board
    board = [' ']*10
   
    tempBoard = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # The Board is numbered as below, You have to enter the number within 1 to 9
    print('Instruction.')
    print('The Board is numbered as below, You have to enter the number within 1 to 9')
    displayBoard(tempBoard)
    playerLetter, computerLetter = getPlayerInput()
    turn = whoGoFirst()
    gameIsPlaying = True

    print('The '+turn+' Will go first.')
    while gameIsPlaying:
        if turn == 'Player':
            #Player turn
            displayBoard(board)
            move = getplayerMove(board)
            makeMove(board,playerLetter,move)
       
            if isWinner(board,playerLetter):
                displayBoard(board)
                print('Hoorayyyy!! You Won the game..')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    displayBoard(board);
                    print('The Game is tie!')
                    break;
                else:
                    turn = 'Computer'
        
        else:
            # Computer Turn
            displayBoard(board)
            move = getComputerMove(board, computerLetter)
            makeMove(board, computerLetter, move)

            if isWinner(board, computerLetter):
                displayBoard(board)
                print('Computer Won the game.. you lose')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    displayBoard(board)
                    print('The Game is Tie!')
                    break;
                else:
                    turn = 'Player'
    if not playAgain():
        break




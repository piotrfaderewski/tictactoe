import os
import sys
import time
#Tictactoe by Tic Tac and Toe

if sys.platform == 'win32':
    clearings = 'cls'
else:
    clearings = 'clear'

#Global value
markX = 'X'
markO = 'O'
EMPTY = ' '
TIE = 'TIE'
NUMofSQR = 9

def displayInstructions():
    """ View game instructions """
    print(
        '''
        
        You are going to choose the number of the field, as shown below:
        \t\t\t-------------
        \t\t\t| 1 | 2 | 3 |
        \t\t\t-------------
        \t\t\t| 4 | 5 | 6 |
        \t\t\t-------------
        \t\t\t| 7 | 8 | 9 |
        \t\t\t-------------
        '''
    )
    
def askYesNo(question):
    """Qustion which answer is yes or no"""
    response = None
    while response not in('y','n'):
        response = input(question).lower()
    return response

def askNumber(question, low, high):
    """Return number from range low - high """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def mark():
    """X or O""" 
    goFirst = askYesNo('Do you want to be entitled to the first move? (y/n): ')
    if goFirst == 'y':
        print('Then you start, as X.')
        player = markX
        computer = markO
    else:
        print('Okay, my turn, you are O.')
        computer = markX
        player = markO
    return computer, player 

def newBoard():
    """ Create new board"""
    board = []
    for i in range(NUMofSQR):
        board.append(EMPTY)
    return board

def drawBoard(board):
    print('-------------')
    print('| %c | %c | %c |' % (board[0], board[1], board[2]))
    print('-------------')
    print('| %c | %c | %c |' % (board[3], board[4], board[5]))
    print('-------------')
    print('| %c | %c | %c |' % (board[6], board[7], board[8]))
    print('-------------')

def possibleMoves(board):
    """Looking for empty squares"""
    moves = []
    for i in range(NUMofSQR):
        if board[i] == EMPTY:
            moves.append(i)
    return moves

def wayToWin(board):
    WAYS_TO_WIN = ( (0,1,2),
                    (3,4,5),
                    (6,7,8),
                    (0,3,6),
                    (1,4,7),
                    (2,5,8),
                    (0,4,8),
                    (2,4,6) )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def playerMove(board, player):
    possible = possibleMoves(board)
    move = None
    while move not in possible:
        move = askNumber('Enter the number of square(1,9): ', 1, 10)
        move -= 1
        if move not in possible:
            print('This field is already taken, choose another one: ')
    print('great')
    return move

def computerMove(board, computer, player):
    #copy board:
    board = board[:]
    #najlepsze pozycje do zajęcia w kolejności: (środek, rogi, reszta)
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)

    print('I am into field number: ', end = ' ')

    #najpierw sprawdzam czy mogę wygrać w danej kolejce
    for move in possibleMoves(board):
        board[move] = computer
        if wayToWin(board) == computer:
            print(move+1)
            return move
        board[move] = EMPTY
    
    #jeśli player moze wygrac
    for move in possibleMoves(board):
        board[move] = player
        if wayToWin(board) == player:
            print(move+1)
            return move
        board[move] = EMPTY
    
    #jeśli nikt nie moze wygrać wybierz najlepsza opcję
    for move in BEST_MOVES:
        if move in possibleMoves(board):
            print(move+1)
            return move
    

def nextTurn(turn):
    if turn == markX:
        return markO
    else:
        return markX

def congratWinner(theWinner, computer, player):
    if theWinner != TIE:
        print(theWinner, 'win !\n')
    else:
        print('Tie!\n')
    
    if theWinner == computer:
        print('As always.')
    elif theWinner == player:
        print('Lucky one.')
    elif theWinner == TIE:
        print('Oh no.')

def play():
    print(
        '''
        \t\t\tTic tac toe
        \t\t\t You vs AI
        '''
    )
    print('\nHere are the tips you need: ')
    displayInstructions()
    time.sleep(1)
    os.system(clearings)

    computer, player = mark()
    turn = markX
    board = newBoard()
    drawBoard(board)

    while not wayToWin(board):
        
        if turn == player:
            move = playerMove(board, player)
            board[move] = player
        else:
            move = computerMove(board, computer, player)
            board[move] = computer

        drawBoard(board)
        
        turn = nextTurn(turn)
    theWinner = wayToWin(board)
    congratWinner(theWinner, computer, player)
    

def main():
    play()
    
    input('To exit press "Return".')

main()


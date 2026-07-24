theBoard = {
            'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '
            }



def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = "X"

for i in range(9): # since there are 9 items  which define the 9 blank squares in the dictionary.
    printBoard(theBoard)
    print("Turn for " + turn + '- Move on which space?')
    move = input()
    theBoard[move] = turn

    if turn == "X":
        turn = '0'
    else:
        turn = 'X'



printBoard(theBoard)

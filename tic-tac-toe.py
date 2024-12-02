board=[
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]


def checkWinner():
    #check for rows
    for row in board:
        if(row[0]==row[1] and row[0]==row[2] and row[0]!='-'):
            return row[0]

    #check for cols    
    for col in range(3):
        if(board[0][col]==board[1][col]==board[2][col] and board[0][col]!='-'):
            return True
    
    #check for diagonal
    if(board[0][0]==board[1][1]==board[2][2] and board[0][0]!='-'):
        return True
    
    if(board[0][2]==board[1][1]==board[2][0] and board[0][2]!='-'):
        return True
    
    #otherwise return false
    return False

def ticTacToe():
    user='O'
    while True:
        print(f'{user} this is your trun')
        r=int(input('select row position from 0-2:'))
        c=int(input('select col position from 0-2:'))
        if (board[r][c]=='O' or board[r][c]=='X'):
            print('the space is already occupied please select another pos...')
            continue

        board[r][c]=user

        for row in board:
            print(row[0],' ',row[1],' ',row[2])

        # cond=checkWinner()
        # print(cond)
        if(checkWinner()):
            print(f'Player {user} You Won The Game...')
            return
        
        if(user=='O'):
            user='X'
        else:
            user='O'

        

# print(board[0][0])
ticTacToe()
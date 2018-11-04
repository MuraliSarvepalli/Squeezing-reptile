#Tic Tac Toe

def print_board(lst):
    print("|{1}|{2}|{3}|\n|{4}|{5}|{6}|\n|{7}|{8}|{9}|".format(*lst))

def check(lst):
    if lst[1]==lst[2]==lst[3]=='X' or lst[1]==lst[2]==lst[3]=='O':
        return 1
    elif lst[4]==lst[5]==lst[6]=='X' or lst[4]==lst[5]==lst[6]=='O':
        return 1
    elif lst[1]==lst[5]==lst[9]=='X' or lst[1]==lst[5]==lst[9]=='O':
        return 1
    elif lst[7]==lst[8]==lst[9]=='X' or lst[7]==lst[8]==lst[9]=='O':
        return 1
    elif lst[3]==lst[5]==lst[7]=='X' or lst[3]==lst[5]==lst[7]=='O':
        return 1
    elif lst[3]==lst[6]==lst[9]=='X' or lst[3]==lst[6]==lst[9]=='O':
        return 1
    elif lst[2]==lst[5]==lst[8]=='X' or lst[2]==lst[5]==lst[8]=='O':
        return 1
    elif lst[1]==lst[4]==lst[7]=='X' or lst[1]==lst[4]==lst[7]=='O':
        return 1
    else:
        return 0

print("Welcome to Tic Tac Toe Game!!!")
tic_tac=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
count=1
pos_lst=[]
player1=input('PLAYER1: Do you want to be X or O?')
if player1=='X':
    player2='O'
else:
    player2='X'
print('player 1 is {}'.format(player1))
print('player 2 is {}'.format(player2))
while len(pos_lst)<9:
    print('player1 turn')
    pos=int(input('Enter the position'))
    if pos in pos_lst:
        print('The position is already occupied, Enter the valid position')
    else:
        pos_lst.append(pos)
        tic_tac[pos]=player1
        print_board(tic_tac)
        chk=check(tic_tac)
    if chk==1:
        print("Congratulations!! Player 1 has won the game")
        break
    if len(pos_lst)==9:
        break
    print('player2 turn')
    pos=int(input('Enter the position'))
    if pos in pos_lst:
        print('The position is already occupied, Enter the valid position')
    else:
        pos_lst.append(pos)
        tic_tac[pos]=player2
        print_board(tic_tac)
        chk=check(tic_tac)
    if chk==1:
        print("Congratulations!! Player 2 has won the game")
        break
if chk==0:
    print("The game is a tie")


#________Bonus point  -------->  "There is a random special move"_______#

import random
bonus = random.randint(0,8)

symbol_1 = None
symbol_2 = None
board = ["0","1","2","3","4","5","6","7","8"]
winnerBox = 0
n = 0

def choose():
    global symbol_1
    global symbol_2

    symbol_1 = input("Player1, choose 'x' or 'o': ")

    if symbol_1 == "x":
        symbol_2 = "o"
    else:
        symbol_2 = "x"




def printBoard(board):
    print(" ",board[0], "|", board[1], "|",board[2])
    print("-------------")
    print(" ",board[3], "|", board[4], "|",board[5])
    print("-------------")
    print(" ",board[6], "|", board[7], "|",board[8])




def round():
    global n
    global board
    global symbol_1
    global symbol_2
    global bonus
    if n % 2 == 0:
        position = int(input("Player_1, enter a number: "))
        if board[position] != "x" and board[position] != "o":
            board[position] = symbol_1
            n = n + 1
        else:
            round()
    else:
        position = int(input("Player_2, enter a number: "))
        if board[position] != "x" and board[position] != "o":
            board[position] = symbol_2
            n = n + 1
        else:
            round()

    if position == bonus:
        n = n - 1
        print("-----BONUS TURN-----")
    




def checkWinner():
    global n
    global board
    global winnerBox
    global symbol_1
    
    for i in range(len(board)):
        if i==0 or i==3 or i==6: 
            if board[i]==board[i+1]==board[i+2]:
                winnerBox = board[i]
                break
        if i==0 or i==1 or i==2:
            if board[i]==board[i+3]==board[i+6]:
                winnerBox = board[i]
                break
        if i==0:
            if board[i]==board[i+4]==board[i+8]:
                winnerBox = board[i]
                break
        if i==2:
            if board[i]==board[i+2]==board[i+4]:
                winnerBox = board[i]
                break

    if winnerBox==0:
        return 0
    
    if symbol_1 == winnerBox:
        print("        player_1 is the __Winner__")
    else:
        print("        player_2 is the __Winner__")
    
    return 1
            
    


def main():
    print("_______There is a random special move_______")
    printBoard(board)
    choose()
    while True:
        round()
        printBoard(board)
        #checkWinner()
        if checkWinner() == 0:
            continue
        else:
            break

main()





    



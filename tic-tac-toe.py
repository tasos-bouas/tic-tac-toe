def DisplayBoard(board):
    row = 0
    for i in range(1,14):
        if i == 1 or i == 5 or i == 9 or i == 13:
            print("+-------+-------+-------+")
        elif i == 2 or i == 4 or i == 6 or i == 8 or i == 10 or i == 12:

                print("|", "|", "|", "|",sep="       ")
        else:

            for column in range(3):

                print("|", board[row][column],"", sep="   ", end="")


            print("|")
            row += 1
    #VictoryFor(board,'X')



def EnterMove(board):
    x = True
    while x:
        ans = int(input("Enter your move: "))
        if ans >= 1 and ans <= 9:
            if any(ans in x for x in board):
                for i in range(3):
                    for j in range(3):
                        if ans == blist[i][j]:
                            a = i
                            b = j
                            break
                    else:
                        continue

                    break
                board[a][b] = "O"
                return
            else:
                print("The field is occupied!")
        else:
            print("Wrong answer!")



def MakeListOfFreeFields(board):
    flist = board[:][:]
    i = 1
    for row in range (3):
        for column in range(3):
            if flist[row][column] == column +i:
                return False
        i += 3
    print("Tie!")
    return True




def VictoryFor(board, sign):
    x = False
    y = False
    if sign == "O":

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == sign:
                x = True

        for j in range(3):
            if sign == board[0][j] == board[1][j] == board[2][j]:
                x = True

        if sign == board[0][0] == board[1][1] == board[2][2] or sign == board[0][2] == board[1][1] == board[2][0]:
            x = True

    else:

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == sign:
                y = True

        for j in range(3):
            if sign == board[0][j] == board[1][j] == board[2][j]:
                y = True

        if sign == board[0][0] == board[1][1] == board[2][2] or sign == board[0][2] == board[1][1] == board[2][0]:
            y = True

    if x == True:
        print("Congratulation You won!")
        return True
    elif y == True:
        print("Computer Won! Don't Worry You Can Try Again!")
        return True
    else:
        return False



def DrawMove(board):
    if a == True:
        x = True
        while x:
            for i in range (1):
                num = randrange(1, 10)

            for i in range(3):
                for j in range(3):
                    if num == board[i][j]:
                        board[i][j] = "X"
                        x = False
        DisplayBoard(board)
    else:
        board[1][1] = "X"
        DisplayBoard(board)
        return True



def clear():
    os.system('clear')




from random import randrange
from time import sleep
import os
while True:
    a = False
    board = []
    i = 1
    for row in range(3):
        x = [column + i for column in range(3)]
        board.append(x)
        i += 3
    blist = board[:][:]
    a = DrawMove(board)

    while VictoryFor(board, "O") == False and VictoryFor(board, "X") == False and MakeListOfFreeFields(board) == False:

        EnterMove(board)
        clear()
        DisplayBoard(board)
        if VictoryFor(board, "O") == True:
            break
        elif VictoryFor(board, "X") == True:
            break
        clear()
        DrawMove(board)
    sleep(2)
    gameon = input('\nDo you want to play again?(Y = YES or N = NO): ')
    if gameon == 'Y' or gameon == 'y':
        continue
    elif gameon == 'N'or gameon == 'n':
        metr = "."
        for i in range(1, 4):
            clear()
            print(f'Terminating The Program{metr * i}')
            sleep(1)

        break
    else:
        clear()
        print('Wrong Answer! Im Going To Terminate The Program!')
        sleep(3)
        metr = "."
        for i in range(1, 4):
            clear()
            print(f'Terminating The Program{metr * i}')
            sleep(1)
        break

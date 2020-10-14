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



def EnterMove(board):
    x = True
    while x:
        ans = int(input("Enter your move: "))
        if ans <= 9:
            for i in range(3):
                for j in range(3):
                    if ans == blist[i][j]:
                        a = i
                        b = j
        else:
            print("Wrong answer!")

        if board[a][b] == "X" or board[a][b] == "O":
            print("The field is occupied")
        else:
            board[a][b] = "O"
            return


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
        print("You won")
        return True
    elif y == True:
        print("Computer Won!")
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








from random import randrange
a = False
board = []
i = 1
for row in range(3):
    x = [column + i for column in range(3)]
    board.append(x)
    i += 3
blist = board[:][:]
print(type(board[0][1]))
a = DrawMove(board)
while VictoryFor(board, "O") == False and MakeListOfFreeFields(board) == False:

    EnterMove(board)
    DisplayBoard(board)
    if VictoryFor(board, "O") == True:
        break
    DrawMove(board)

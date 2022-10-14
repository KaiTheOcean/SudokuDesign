import json

def getFile():
    difficulty = ''
    while difficulty != "easy" or difficulty != "medium" or difficulty != "hard":
        difficulty = input("Which difficulty would you like to play? [easy, medium, hard] ")
        if difficulty.lower() == "easy":
            return "131.05.Easy.json"
        elif difficulty.lower() == "medium":
            return "131.05.Medium.json"
        elif difficulty.lower() == "hard":
            return "131.05.Medium.json"
        else: 
            print("You have enter the wrong input")
            print("Please enter it again")

def readFile(fileName):
    with open(fileName, "r") as file:
        data = json.load(file)
    board = data["board"]
    return board

def saveFile(fileName, board):
    data = {
        "board": board
    }
    with open(fileName, "w") as file:
        json.dump(data, file)

def row_check(board):
    for row in board:
        if len(set(row)) == len(row):
            for i in range(len(row)):
                if row[i] in row:
                    continue
                else:
                    return False
        else:
            return False
    return True

def column_check(board): 
    cols = []
    check = []
    for i in range(1, len(board)+1):
        check.append(i)
    for row in range(len(board)):
        for column in board:
            cols += [column[row]]
        cols.sort()
        for i in range(len(cols)):
            if  cols[i] != check[i]:
                return False
        cols = []
    return True

# This needs to be modified, it's only for the top left region
def square_check(board):
    square = []
    new_square = []
    check = []
    for i in range(1, len(board)+1):
        check.append(i)
    for row in range(3):
        firstThree = board[row]
        square.append(firstThree[0:3])
    print(square)
    for i in square:
        for j in i:
            new_square.append(j)
    new_square.sort()
    print(new_square)
    for i in range(len(check)):
        if new_square[i] != check[i]:
            return False
    return True

def position_check(position):
    position_list = []
    for i in position:
        position_list.append(i.upper())
    for i in position_list:
        if position_list[0].isdigit():
            position_list[0], position_list[1] = position_list[1], position_list[0]
    letter_dictionary = {"A": "0",
                       "B": "1",
                       "C": "2",
                       "D": "3",
                       "E": "4",
                       "F": "5",
                       "G": "6",
                       "H": "7",
                       "I": "8"}
    if position_list[0] in letter_dictionary.keys():
        position_list[0] = letter_dictionary[position_list[0]]
    return position_list

def displayBoard(board):
    print()
    print("   A  B  C D  E  F G  H  I ")
    for row in range(len(board)):
        for column in range(len(board)):
            # print(board[row][column])
            print(row)
        # print(f"{row+1}  {board[row][0]}  {board[row][1]}  {board[row][2]}|{board[row][3]}  {board[row][4]}  {board[row][5]}|{board[row][6]}  {board[row][7]}  {board[row][8]}")
        # if row+1 == 3 or row+1 == 6:
        #     print("  - - - - +- - - - +- - - -") 

fileName = getFile()
board = readFile(fileName)
displayBoard(board)

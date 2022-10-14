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

def position_check(position):
    '''Modify the user input
       if the use enters A1, then return 01
       if the user enters 1A then return 01
       the first element in the position list 
       is always the column and the second element 
       is always the row'''
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

def displayBoard(board):
    print()
    print("   A  B  C D  E  F G  H  I ")
    for row in range(9):
        if row == 3 or row == 6:
            print("- - + - - + - - +")
        else:
            print(row+1, end='')
        for column in range(10):
            separator = "   |    | \n"
            if column == 9:
                print(sep='\n')
            else:
                print(board[row][column] or ' ', end='', sep = separator)

def update_board(position_list, value, board):
    # column = int((position_list[0]))
    # row = int((position_list[1]))
    board[0][0] == value  
    return board

fileName = getFile()
board = readFile(fileName)
displayBoard(board)
position = input("Type a position: ")
positoin_list = position_check(position)
value = input("What is the value for that position: ")
print(update_board(positoin_list, value, board))
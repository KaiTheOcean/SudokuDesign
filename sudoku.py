# 1. Name:
#      Kaidi Zhang
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      For now this program will allow users to input data, and 
#      the system will save the data will the user quites the game
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was to display the board in the right format
# 5. How long did it take for you to complete the assignment?
#      Maybe 2 hours

import json

def getFile():
    '''Receive the file according to the difficulty from user'''

    difficulty = ''
    while difficulty != "easy" or difficulty != "medium" or difficulty != "hard":
        difficulty = input("Which difficulty would you like to play? [easy, medium, hard] ")
        if difficulty.lower() == "easy": # Easy difficulty
            return "131.05.Easy.json"
        elif difficulty.lower() == "medium": # Medium difficulty
            return "131.05.Medium.json"
        elif difficulty.lower() == "hard": # Hard difficulty
            return "131.05.Medium.json"
        else: 
            print("You have enter the wrong input")
            print("Please enter it again")

def readFile(fileName):
    '''Convert the json file into a list'''
    with open(fileName, "r") as file:
        data = json.load(file)
    board = data["board"]
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                board[row][column] = ' '
    return board

def saveFile(fileName, board):
    '''Save the board into a json file'''
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
    print("   A  B  C  D  E  F  G  H  I ")
    for row in range(9):
        if row == 3 or row == 6:
            print("  - - - - + - - - - + - - - - +")
            print(row+1, end='')
        else:
            print(row+1, end='')
        for column in range(10):
            if column == 9:
                print(sep='\n')
            elif column == 3 or column == 6:
                print("|", end='')
                print(str(board[row][column]).rjust(2), end='')
            else:
                print(str(board[row][column]).rjust(3), end='')

def update_board(position_list, value, board):
    column = int((position_list[0]))
    row = int((position_list[1]))
    board[row-1][column] = value 
    return board

def playGame():
    fileName = getFile()
    board = readFile(fileName)
    displayBoard(board)
    while True:
        print("Specify a coordinate to edit or 'Q' to save and quit: ")
        position = input("-> ")
        if position.upper() == "Q":
            return False
        else:
            positoin_list = position_check(position)
            value = int(input("What number goes in " + position + " ? "))
            update_board(positoin_list, value, board)
            displayBoard(board)
            saveFile(fileName, board)

playGame()

# Test Cases: B8 - 8, E5 - 8, and quit save the board

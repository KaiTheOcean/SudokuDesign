# 1. Name:
#      Kaidi Zhang
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      This program will allow player to play the sudoku game
# 4. What was the hardest part? Be as specific as possible.
#       
# 5. How long did it take for you to complete the assignment?
#      

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
    letter_dictionary = {"A": 0,
                       "B": 1,
                       "C": 2,
                       "D": 3,
                       "E": 4,
                       "F": 5,
                       "G": 6,
                       "H": 7,
                       "I": 8}
    if position_list[0] in letter_dictionary.keys():
        position_list[0] = letter_dictionary[position_list[0]]
    return position_list

def row_check(board):
    '''Check the row to see if is complete'''

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
    '''Check to see the column is complete or not'''

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

def column_hint(board, position_list):
    '''Give the user hint of what are the available numbers for this column'''

    # Create a check list 
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Get the user selected position's column value
    current_column_index = int(position_list[0])
    current_column_value = []
    for row in range(9):
        current_column_value.append(board[row][current_column_index])

    # compare with the check list and remove duplicates
    for i in range(len(current_column_value)):
        if current_column_value[i] in check_list:
            check_list.remove(current_column_value[i])

    # It returns all the posibile value for the column
    return check_list

def row_hint(board, position_list):
    '''Give the user hint of what are the available numbers for this row'''

    # Create a check list
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Get the user selected position's row value
    current_row_index = int(position_list[1])
    current_row_value = board[current_row_index - 1]

    # Compare with check list, and remove the duplicates
    for i in range(len(current_row_value)):
        if current_row_value[i] in check_list:
            check_list.remove(current_row_value[i])

    # It returns all the possible value for the row
    return check_list
    
def square_hint(board, position_list):
    '''Give the user hint of the available numbers for this square'''

    # Set the variables and check list
    column_index = int(position_list[0])
    row_index = int(position_list[1])
    column_index = column_index + 1
    row_index = row_index
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Use if statement to defualt the row, column indexes
    if 1 <= row_index <= 3:
        row_index = 3
    elif 4 <= row_index <= 6:
        row_index = 6
    elif 7 <= row_index <= 9:
        row_index = 9

    if 1 <= column_index <= 3:
        column_index = 3
    elif 4 <= column_index <= 6:
        column_index = 6
    elif 7 <= column_index <= 9:
        column_index = 9

    # Store the selected square's value into a list
    square_value = []
    for i in range(row_index-3, row_index):
        for j in range(column_index-3, column_index):
            square_value.append(board[i][j])

    # Compare the sqaure_value with the check list 
    for i in range(len(square_value)):
        if square_value[i] in check_list:
            check_list.remove(square_value[i])

    # It returns all the possible value for the square
    return check_list

def hint(board, position_list):
    '''It finds out the possible value according to its 
       row, column and sqaure'''

    # Get row value, column value, and square value
    row_hint_list = row_hint(board, position_list)
    column_hint_list = column_hint(board, position_list)
    square_hint_list = square_hint(board, position_list)

    # Set check list to compare
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Put all the possible values togehter and compare it with check list 
    # If all three hint list's elements are in check list then save them
    # otherwise remove them.
    hint_list = []
    for check in check_list:
        if (check in row_hint_list) and (check in column_hint_list) \
            and (check in square_hint_list):
            hint_list.append(check)
    print("The available values are: " + str(hint_list))
    return True
    
def displayBoard(board):
    '''Display the board for user'''
    print()
    print("   A  B  C  D  E  F  G  H  I ")

    # Within a for loop, do the following when it meets the 
    # if statement conditions
    for row in range(9):
        if row == 3 or row == 6:
            print("  - - - - + - - - -+ - - - - ")
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
    '''Update the board according to the user's input 
        position and value'''

    column = int((position_list[0]))
    row = int((position_list[1]))
    board[row-1][column] = value 
    return board

def sqaure_filled(board, position_list):
    '''Check if the position is already filled'''

    column = int(position_list[0])
    row = int(position_list[1])
    row = row - 1
    if board[row][column] != " ":
        print("You can't enter in this position!")
        return False
    else:
        return True

def valid_input(position):
    letter_check = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    number_check = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if position.lower() == "q":
        return True
    elif position[0].upper() in letter_check and position[1] in number_check:
        return True   
    elif position[1].upper() in letter_check and position[0] in number_check:
        return True
    else:
        print("Make sure you enter the correct information (rihgt coordinates, and q to quite)")
        return False

def unique_row(board, value, position_list):
    '''Check to make sure the value isn't matching the numbers on this row'''

    row_index = int(position_list[1])
    row_index = row_index - 1
    current_row = []
    for column in range(9):
        current_row.append(board[row_index][column])
    if value not in current_row:
        return True
    else:
        print(str(value) + " is already exist in this row")
        return False

def unique_column(board, value, position_list):
    '''Check to make sure the value isn't matching the numbers on this column'''
    column_index = int(position_list[0])
    current_column = []
    for row in range(9):
        current_column.append(board[row][column_index])
    if value not in current_column:
        return True
    else:
        print(str(value) + " is already exist in this column")
        return False

def unique_inside_sqaure(board, value, position_list):
    '''Check to make sure the value isn't matching the numers in this sqaure'''

    # Set the variables
    column_index = int(position_list[0])
    row_index = int(position_list[1])
    column_index = column_index + 1
    row_index = row_index

    # Use if statement to defualt the row, column indexes
    if 1 <= row_index <= 3:
        row_index = 3
    elif 4 <= row_index <= 6:
        row_index = 6
    elif 7 <= row_index <= 9:
        row_index = 9

    if 1 <= column_index <= 3:
        column_index = 3
    elif 4 <= column_index <= 6:
        column_index = 6
    elif 7 <= column_index <= 9:
        column_index = 9

    # Store the selected square's value into a list
    square_value = []
    for i in range(row_index-3, row_index):
        for j in range(column_index-3, column_index):
            square_value.append(board[i][j])

    if value not in square_value:
        return True
    else:
        print(str(value) + " is already exist in this square")
        return False

def valid_number(board, value, position_list):
    '''make sure the user only enter the value from 1 - 9''' 
    value = int(value)
    check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if value <= 0 or value >= 10:
        print("Make sure the value is in between 1 and 9")
        return False
    if unique_row(board, value, position_list):
        if unique_column(board, value, position_list):
            if unique_inside_sqaure(board, value, position_list):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def playGame():
    '''Start the game'''

    # Receive the file name and display it as a sudoku broad
    fileName = getFile()
    board = readFile(fileName)
    displayBoard(board)

    while True:
        
        # Ask the user for either a coordinate or Q to quie or S for hint
        print("Specify a coordinate to edit ,'q' to save and quit ")
        position = input("-> ")
        print()

        # Quit the game
        if position.lower() == "q":
            # saveFile(fileName, board)
            print("See you next time!")
            return False

        # Valid the position
        if not valid_input(position):
            continue

        # Convert the position into a useful list
        position_list = position_check(position)

        # Check if the suqare is been filled or not
        if not sqaure_filled(board, position_list):
            continue

        else:

            # Ask for what value goes into that square
            value = input("What number goes in " + position + " ? or (type s for hint) ")

            # Show the hint
            if value.lower() == "s":
                hint(board, position_list)
                continue

            # Valid the value from the user
            if not valid_number(board, value, position_list):
                continue
            
            # Do updates on the board
            update_board(position_list, value, board)

            # Display the board
            displayBoard(board)

            # Save the file
            saveFile(fileName, board)

playGame()


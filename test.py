# # board = [[0,1,2,3], [4,5,6,7], [8, 9, 10, 11], [0,0,0,0]]
# # if board[1][1] != 0:
# #     print("Cant")
# # else:
# #     print("can")
# # for i in range(len(board)):
# #     for j in range(len(board)):
# #         if board[i][j] == 0:
# #             board[i][j] = "a"
# # print(board)
# # board[0][0] = "a"
# # print(board)

# board = [[7, 2, 3, " ", " ", " ", 1, 5, 9], [6, " ", " ", 3, " ", 2, " ", " ", 8], [0, 0, 0, 0]]
# # position = [2, 2]
# # column_index = position[1]
# # column_value = []
# # for i in range(len(board[0]) -1):
# #     column_value.append(board[i][column_index])
# # print(column_value)
# import json 
import json

# def getFile():
#     '''Receive the file according to the difficulty from user'''

#     difficulty = ''
#     while difficulty != "easy" or difficulty != "medium" or difficulty != "hard":
#         difficulty = input("Which difficulty would you like to play? [easy, medium, hard] ")
#         if difficulty.lower() == "easy": # Easy difficulty
#             return "131.05.Easy.json"
#         elif difficulty.lower() == "medium": # Medium difficulty
#             return "131.05.Medium.json"
#         elif difficulty.lower() == "hard": # Hard difficulty
#             return "131.05.Medium.json"
#         else: 
#             print("You have enter the wrong input")
#             print("Please enter it again")

# def readFile(fileName):
#     '''Convert the json file into a list'''
#     with open(fileName, "r") as file:
#         data = json.load(file)
#     board = data["board"]
#     for row in range(len(board)):
#         for column in range(len(board)):
#             if board[row][column] == 0:
#                 board[row][column] = ' '
#     return board

# def displayBoard(board):
#     print()
#     print("   A  B  C  D  E  F  G  H  I ")
#     for row in range(9):
#         if row == 3 or row == 6:
#             print("  - - - - + - - - - + - - - - +")
#             print(row+1, end='')
#         else:
#             print(row+1, end='')
#         for column in range(10):
#             if column == 9:
#                 print(sep='\n')
#             elif column == 3 or column == 6:
#                 print("|", end='')
#                 print(str(board[row][column]).rjust(2), end='')
#             else:
#                 print(str(board[row][column]).rjust(3), end='')

# def unique_column(board, value, position_list):
#     '''Check to make sure the value isn't matching the numbers on this column'''
#     column_index = int(position_list[0])
#     current_column = []
#     for row in range(9):
#         current_column.append(board[row][column_index])
#     if value not in current_column:
#         return True
#     else:
#         print(str(value) + " is already exist in this column")
#         return False

# fileName = getFile()
# board = readFile(fileName)
# print(board)
# displayBoard(board)
# unique_column(board, 7, "03")

# # first square
# # row = 3
# # column = 0

# # second square
# row = 5
# column = 1

# # thrid square 
# # row = 4
# # column = 0

# if 0 <= row <= 3:
#     row = 3
# elif 4 <= row <= 6:
#     row = 6
# elif 7 <= row <= 9:
#     row = 9

# if 0 <= column <= 3:
#     column = 3
# elif 4 <= column <= 6:
#     column = 6
# elif 7 <= column <= 9:
#     column = 9

# check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list = []
# for i in range(row-3, row):
#     for j in range(column-3, column):
#         list.append(board[i][j])

# for i in range(len(list)):
#         if list[i] in check_list:
#             check_list.remove(list[i])
# print(check_list)

# s = input(" ")
# print(s.upper())
# list = ["A"]
# if s[0].upper() in list:
#     print("Hi")


# def dollarFromEuro(euro):
#     assert euro >= 0, "It gotta be equal or greater than 0"
#     return 1.13 * euro

# print(dollarFromEuro(-1))

# Test Cases 
# negative euro, gives me error
# 

def computePay(wage, hours):
    if 0 <= hours <= 40:
        return wage * hours
    elif 168 >= hours > 40:
        return (wage * 40) + wage * 1.5 * (hours - 40)


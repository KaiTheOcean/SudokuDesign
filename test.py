# board = [[0,1,2,3], [4,5,6,7], [8, 9, 10, 11], [0,0,0,0]]
# if board[1][1] != 0:
#     print("Cant")
# else:
#     print("can")
# for i in range(len(board)):
#     for j in range(len(board)):
#         if board[i][j] == 0:
#             board[i][j] = "a"
# print(board)
# board[0][0] = "a"
# print(board)

board = [[7, 2, 3, " ", " ", " ", 1, 5, 9], [6, " ", " ", 3, " ", 2, " ", " ", 8], [0, 0, 0, 0]]
# position = [2, 2]
# column_index = position[1]
# column_value = []
# for i in range(len(board[0]) -1):
#     column_value.append(board[i][column_index])
# print(column_value)

check_list = [1, 2, 3, 4, 5,6 ,7, 8, 9]
current_row = board[1]
for i in range(len(check_list)):
    if current_row[i] in check_list:
        check_list.remove(current_row[i])
print(check_list)

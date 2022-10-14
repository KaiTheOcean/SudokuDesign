board = [[0,1,2,3], [4,5,6,7], [8, 9, 10, 11], [0,0,0,0]]
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == 0:
            board[i][j] = "a"
print(board)
board[0][0] = "a"
print(board)
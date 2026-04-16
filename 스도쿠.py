def is_valid(board,row,col,num):
    for i in range(9):
        if board[i][col] == num:
            return False
    
    for i in range(9):
        if board[row][i] == num:
            return False

    row = row //3 *3
    col = col //3 *3

    for i in range(row,row+3):
        for j in range(col,col+3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for m in range(9):
        for l in range(9):
            if board[m][l] == 0:
                for n in range(1, 10):
                    if is_valid(board,row=m,col=l,num=n):
                        board[m][l] = n
                        if solve_sudoku(board):
                            return True
                        board[m][l] = 0 
                return False  
    return True

    

problem = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

if solve_sudoku(problem):
    print(problem)
else:
    print('문제를 해결할 수 없습니다.')
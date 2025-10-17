def n_queens_recursion(n):
    def backtrack(row, board, solutions):
        if row == n:
            solutions.append(board[:]) 
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board, solutions)
                board[row] = -1
    
    solutions = []
    board = [-1] * n 
    backtrack(0, board, solutions)
    return solutions

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True
inp = int(input())
print(len(n_queens_recursion(inp)))

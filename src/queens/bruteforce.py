import itertools

def is_valid(board):
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def n_queens_bruteforce(n):

    solutions = 0
    for permutation in itertools.permutations(range(n)):
        if is_valid(permutation):
            solutions += 1
    return solutions

inp = int(input())
print(n_queens_bruteforce(inp))


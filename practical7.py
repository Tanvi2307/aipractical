N = 8 
board = [-1] * N 
 
def is_safe(row, col): 
    for r in range(row): 
        c = board[r] 
 
        if c == col or abs(r - row) == abs(c - col): 
            return False 
 
    return True 
 
def solve(row): 
    if row == N: 
        return True 
 
    for col in range(N): 
        if is_safe(row, col): 
            board[row] = col 
 
            if solve(row + 1): 
                return True 
 
            board[row] = -1 
 
    return False 
 
if solve(0): 
    print("Solution for 8-Queens:") 
 
    for row in range(N): 
        for col in range(N): 
            if board[row] == col: 
                print("Q", end=" ") 
            else: 
                print(".", end=" ") 
        print() 
else: 
    print("No solution found.") 
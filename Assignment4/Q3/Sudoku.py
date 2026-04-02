def show_grid(g):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            print(g[r][c], end=" ")
        print()

def check(g, r, c, v):
    for x in range(9):
        if g[r][x] == v:
            return False

    for x in range(9):
        if g[x][c] == v:
            return False

    sr = r - r % 3
    sc = c - c % 3

    for i in range(3):
        for j in range(3):
            if g[sr + i][sc + j] == v:
                return False

    return True

def locate(g):
    for r in range(9):
        for c in range(9):
            if g[r][c] == 0:
                return r, c
    return None

def backtrack(g):
    pos = locate(g)
    if not pos:
        return True

    r, c = pos

    for v in range(1, 10):
        if check(g, r, c, v):
            g[r][c] = v

            if backtrack(g):
                return True

            g[r][c] = 0

    return False


grid = [
    [0,0,3,0,2,0,6,0,0],
    [9,0,0,3,0,5,0,0,1],
    [0,0,1,8,0,6,4,0,0],
    [0,0,8,1,0,2,9,0,0],
    [7,0,0,0,0,0,0,0,8],
    [0,0,6,7,0,8,2,0,0],
    [0,0,2,6,0,9,5,0,0],
    [8,0,0,2,0,3,0,0,9],
    [0,0,5,0,1,0,3,0,0]
]

print("Sudoku Puzzle:\n")
show_grid(grid)

if backtrack(grid):
    print("\nSolved Sudoku:\n")
    show_grid(grid)
else:
    print("No solution exists.")
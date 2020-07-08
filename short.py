def solve(grid, i=0):
    if i == 81: return True
    if grid[i] != 0: return solve(grid, i+1)
    for v in range(1, 10):
        if all(all([grid[j*9+i%9]!=v,grid[(i//9)*9+j]!=v,grid[((j//3)+(i//27)*3)*9+((i%9)//3)*3+j%3]!=v]) for j in range(9)):
            grid[i] = v
            if solve(grid, i+1): return True
    grid[i] = 0
    return False
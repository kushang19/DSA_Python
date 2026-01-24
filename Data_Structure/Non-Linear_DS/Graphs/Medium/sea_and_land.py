# ========================== sea and land =============================

def sea_land(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r,c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != 1:
            return

        grid[r][c] = "#"

        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
   

    for i in range(rows):
        if grid[i][0] == 1:
            dfs(i,0)
        if grid[i][cols-1] == 1:
            dfs(i,cols-1)
           
    for j in range(cols):
        if grid[0][j] == 1:
            dfs(0,j)
        if grid[rows-1][j] == 1:
            dfs(rows-1, j)

    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count+=1

    return count

print(sea_land([
    [0,0,0,0],
    [1,0,1,0],
    [0,1,1,0],
    [0,0,0,0]
]))
print(sea_land([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]) )

print(sea_land([[0,1,0],[1,1,0],[0,0,0],[0,1,0],[0,0,0]]) )
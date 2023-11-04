def findIslands(y, x):
    if y >= M or y <= -1 or x >= N or x <= -1:
        return False
    
    if grid[y][x] == "1":
        grid[y][x] = "0"

        findIslands(y-1, x)
        findIslands(y+1, x)
        findIslands(y, x-1)
        findIslands(y, x+1)

        return True
    return False



grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

# grid = [["1","0","1","1","0","1","1"]]

result = 0
M = len(grid)
N = len(grid[0])
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if findIslands(i, j) == True:
            result += 1

print(result)
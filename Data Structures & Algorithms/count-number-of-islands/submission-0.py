class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        countIslands = 0
        def removeIsland(x, y):
            if x-1 >= 0 and grid[x-1][y] == "1":
                grid[x-1][y] = 0
                removeIsland(x-1, y)
            if y-1 >= 0 and grid[x][y-1] == "1":
                grid[x][y-1] = 0
                removeIsland(x, y-1)
            if x+1 < len(grid) and grid[x+1][y] == "1":
                grid[x+1][y] = 0
                removeIsland(x+1, y)
            if y+1 < len(grid[0]) and grid[x][y+1] == "1":
                grid[x][y+1] = 0
                removeIsland(x, y+1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    countIslands+=1
                    removeIsland(i,j)
        return countIslands



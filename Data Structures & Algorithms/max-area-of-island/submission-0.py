class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        def removeIsland(x,y):
            curr = 0
            if x+1<len(grid) and grid[x+1][y] == 1:
                curr +=1
                grid[x+1][y] = 0
                curr+=removeIsland(x+1,y)
            if y+1<len(grid[0]) and grid[x][y+1] == 1:
                curr +=1
                grid[x][y+1] = 0
                curr+=removeIsland(x,y+1)
            if y-1>=0 and grid[x][y-1] == 1:
                curr +=1
                grid[x][y-1] = 0
                curr += removeIsland(x,y-1)
            if x-1>=0 and grid[x-1][y] == 1:
                curr +=1
                grid[x-1][y] = 0
                curr += removeIsland(x-1,y)
            return curr
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    currArea = 1+removeIsland(i,j)
                    maxArea = max(maxArea,currArea)
        return maxArea
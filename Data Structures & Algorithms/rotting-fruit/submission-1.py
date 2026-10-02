class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        v = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    v.append((i,j))
        

        while len(v) > 0:
            vNew = []
            inc = False
            for x,y in v:
                if x+1 < len(grid) and grid[x+1][y] == 1:
                    grid[x+1][y] = 2
                    vNew.append((x+1, y))
                    inc = True
                if x-1 >= 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    vNew.append((x-1, y))
                    inc = True
                if y-1 >= 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    vNew.append((x, y-1))
                    inc = True
                if y+1 < len(grid[0]) and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    vNew.append((x, y+1))
                    inc = True
                grid[x][y] = 0
            v = vNew
            if inc:
                count+=1
            print(grid)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
            
        return count



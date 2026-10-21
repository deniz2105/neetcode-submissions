class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        q = deque()
        q.append(((0,0),1))

        dirs = [(-1,0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1,1)]

        while len(q) >0:
            pos, stepCount = q.popleft()
            
            if pos[0] == len(grid)-1 and pos[1] == len(grid[0])-1 and grid[pos[0]][pos[1]] == 0:
                return stepCount
            grid[pos[0]][pos[1]] = 1
            for x,y in dirs:
                if 0 <= pos[0] + x < len(grid) and 0 <= pos[1] + y < len(grid[0]) and grid[pos[0]+x][pos[1]+y] == 0:
                    q.append(((pos[0] + x, pos[1]+y), stepCount+1))
        return -1


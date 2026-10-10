class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        v = set()
        q = deque()
        if grid[0][0] == 1:
            return -1
        q.append((0,0))

        dist = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]
        dist[0][0] = 1
        v.add((0,0))
        while len(q)> 0:
            x,y = q.pop()
            
            if x == len(grid)-1 and y == len(grid[0])-1:
                if grid[x][y] == 1:
                    return -1
                else:
                    return dist[x][y]
            if x+1 < len(grid) and grid[x+1][y] == 0 and (x+1, y) not in v:
                q.appendleft((x+1, y))
                dist[x+1][y] = dist[x][y] +1
                v.add((x+1,y))
            if x-1 >= 0 and grid[x-1][y] == 0 and (x-1, y) not in v:
                q.appendleft((x-1, y))
                dist[x-1][y] = dist[x][y] +1
                v.add((x-1,y))
            if y+1 < len(grid[0]) and grid[x][y+1] == 0 and (x, y+1) not in v:
                q.appendleft((x, y+1))
                dist[x][y+1] = dist[x][y] +1
                v.add((x,y+1))
            if y-1 >= 0 and grid[x][y-1] == 0 and (x, y-1) not in v:
                q.appendleft((x, y-1))
                dist[x][y-1] = dist[x][y] +1
                v.add((x,y-1))
            if y-1 >= 0 and x-1 >= 0 and grid[x-1][y-1] == 0 and (x-1, y-1) not in v:
                q.appendleft((x-1, y-1))
                dist[x-1][y-1] = dist[x][y] +1
                v.add((x-1,y-1))
            if y-1 >= 0 and x+1 < len(grid) and grid[x+1][y-1] == 0 and (x+1, y-1) not in v:
                q.appendleft((x+1, y-1))
                dist[x+1][y-1] = dist[x][y] +1
                v.add((x+1,y-1))
            if y+1 < len(grid[0])and x-1 >= 0 and grid[x-1][y+1] == 0 and (x-1, y+1) not in v:
                q.appendleft((x-1, y+1))
                dist[x-1][y+1] = dist[x][y] +1
                v.add((x-1,y+1))
            if y+1 < len(grid[0]) and x+1 < len(grid) and grid[x+1][y+1] == 0 and (x+1, y+1) not in v:
                q.appendleft((x+1, y+1))
                dist[x+1][y+1] = dist[x][y] +1
                v.add((x+1,y+1))
        return -1
                


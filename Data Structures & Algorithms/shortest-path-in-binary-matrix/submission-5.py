class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        visited = set()
        if grid[0][0] == 1:
            return -1
        q = deque()
        count =0
        minCount = float('inf')
        x,y = 0,0
        q.append((x,y))
        visited.add((x,y))
        counts = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]
        counts[0][0]=1
        while len(q) > 0:
            x,y = q.popleft()

            
            if x+1 < len(grid) and (x+1,y) not in visited and grid[x+1][y] == 0:
                q.append((x+1,y))
                visited.add((x+1,y))
                counts[x+1][y] = min(counts[x][y] +1, counts[x+1][y])
            if y+1 < len(grid[0]) and (x,y+1) not in visited and grid[x][y+1] == 0:
                q.append((x,y+1))
                visited.add((x,y+1))
                counts[x][y+1] = min(counts[x][y] +1, counts[x][y+1])
            if x+1 < len(grid) and y+1 < len(grid[0]) and (x+1,y+1) not in visited and grid[x+1][y+1] == 0:
                q.append((x+1,y+1))
                visited.add((x+1,y+1))
                counts[x+1][y+1] = min(counts[x][y] +1, counts[x+1][y+1])
            if x-1 >= 0 and y+1 < len(grid[0]) and (x-1,y+1) not in visited and grid[x-1][y+1] == 0:
                q.append((x-1,y+1))
                visited.add((x-1,y+1))
                counts[x-1][y+1] = min(counts[x][y] +1, counts[x-1][y+1])
            if x-1 >= 0 and y-1>= 0 and (x-1,y-1) not in visited and grid[x-1][y-1] == 0:
                q.append((x-1,y-1))
                visited.add((x-1,y-1))
                counts[x-1][y-1] = min(counts[x][y] +1, counts[x-1][y-1])
            if x+1 < len(grid) and y-1>= 0 and (x+1,y-1) not in visited and grid[x+1][y-1] == 0:
                q.append((x+1,y-1))
                visited.add((x+1,y-1))
                counts[x+1][y-1] = min(counts[x][y] +1, counts[x+1][y-1])
            if x-1 >= 0 and (x-1,y) not in visited and grid[x-1][y] == 0:
                q.append((x-1,y))
                visited.add((x-1,y))
                counts[x-1][y] = min(counts[x][y] +1, counts[x-1][y])
            if y-1 >= 0 and (x,y-1) not in visited and grid[x][y-1] == 0:
                q.append((x,y-1))
                visited.add((x,y-1))
                counts[x][y-1] = min(counts[x][y] +1, counts[x][y-1])
            print(counts)
            if x == len(grid)-1 and y == len(grid[0])-1:
                break
        
        if x != len(grid)-1 or y != len(grid[0])-1:
            return -1
        return counts[len(grid)-1][len(grid[0])-1]
            
            

            


            



class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        
        pq = []
        heapq.heappush(pq,(grid[0][0], (0,0)))
        timePassed = 0
        currElevation = grid[0][0]
        dirs = ((0,1),(1,0),(-1,0),(0,-1))
        visited = set()
        while pq:
            currElevation, loc =heapq.heappop(pq)
            
            if loc[0] == len(grid)-1 and loc[1] == len(grid[0])-1:
                return currElevation
            for d in dirs:
                newR = d[0]+loc[0]
                newC = d[1] + loc[1]
                if (newR, newC) not in visited and 0<=newR<len(grid) and 0<=newC<len(grid):
                    elevationDiff = grid[newR][newC] - currElevation
                    if elevationDiff < 0:
                        elevationDiff=0
                    heapq.heappush(pq,(currElevation + elevationDiff, (newR, newC)))
                    visited.add((newR, newC))
        return -1



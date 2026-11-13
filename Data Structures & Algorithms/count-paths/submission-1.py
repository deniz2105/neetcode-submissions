class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        
        dirs = ((-1,0),(0,-1))
        for i in range(n):
            cache[0][i] = 1
        for i in range(m):
            cache[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                for d in dirs:
                    cache[i][j] +=cache[i+d[0]][j+d[1]]
        return cache[-1][-1]

                
                


        



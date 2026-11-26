class Solution:
    def solve(self, board: List[List[str]]) -> None:
        idxs = []
        for i in range(len(board)):
            if board[i][0] == 'O':
                idxs.append((i,0))
            if board[i][-1] == 'O':
                idxs.append((i,len(board[0])-1))
        for i in range(len(board[0])):
            if board[0][i] == 'O':
                idxs.append((0, i))
            if board[-1][i] == 'O':
                idxs.append((len(board)-1, i))
                        
        
        visited = set()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(i,j):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for x,y in dirs:
                if 0<=i+x<len(board) and 0<=y+j<len(board[0]) and (i+x, j+y) not in visited and board[i+x][j+y] == 'O':
                    dfs(i+x, j+y)
        
        for i, j in idxs:
            dfs(i,j)
        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'

            
            


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsSet = set(words)
        letterDict = {}
        letterDict["#"] = {}
        for word in words:
            if word[0] not in letterDict["#"]:
                letterDict["#"][word[0]] = {}
            currDict = letterDict["#"][word[0]]
            for i in range(1,len(word)):
                if word[i] not in currDict:
                    currDict[word[i]] = {}
                currDict = currDict[word[i]]
        
        resp = set()
        dirs = ((0,-1),(-1,0),(1,0),(0,1))
        visiting = set()
        def dfs(i, j, currString, currDict):
            if currString in wordsSet:
                resp.add(currString)
            if len(currDict.items())==0:
                return
            
            for d in dirs:
                nextRow = d[0] + i
                nextCol = d[1] + j
                if 0<= nextRow < len(board) and 0<= nextCol < len(board[0]) and (nextRow, nextCol) not in visiting and board[nextRow][nextCol] in currDict:
                    visiting.add((nextRow, nextCol))
                    dfs(nextRow, nextCol, currString +board[nextRow][nextCol], currDict[board[nextRow][nextCol]])
                    visiting.remove((nextRow, nextCol))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in letterDict["#"]:
                    visiting.add((i,j))
                    dfs(i,j,board[i][j], letterDict["#"][board[i][j]])
                    visiting.remove((i,j))
        return list(resp)
                    


            



        

        return []
                

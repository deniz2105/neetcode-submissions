class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = []
        maxLen = 0
        for i in range(0, len(words)):
            currLen = len(words[i])
            maxLen = max(maxLen, currLen)
        if maxLen != len(words):
            return False
        for i in range(0, maxLen):
            currWord = ""
            for j in range(len(words)):
                if i <= len(words[j])-1:
                    currWord += words[j][i]
                else:
                    break
            cols.append(currWord)
        
        for i in range(len(words)):
            if words[i]!=cols[i]:
                return False
            
        return True

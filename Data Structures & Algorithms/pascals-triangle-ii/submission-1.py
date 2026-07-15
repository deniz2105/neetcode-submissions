class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = [1,1]
        if rowIndex == 1:
            return prev
        
        for i in range(2, rowIndex+1):
            curr = [0] * (len(prev)+1)
            curr[0] = prev[0]
            curr[len(curr)-1] = prev[len(prev)-1]
            for j in range(1, len(prev)):
                curr[j] = prev[j] + prev[j-1]
            prev = curr
        return prev

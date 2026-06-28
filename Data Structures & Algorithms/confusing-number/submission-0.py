class Solution:
    def confusingNumber(self, n: int) -> bool:
        numList = []
        numDict = {}
        numDict[0] = 0
        numDict[1] = 1
        numDict[6] = 9
        numDict[8] = 8
        numDict[9] = 6
        tmp = n

        while tmp > 0:
            curr = tmp %10
            if curr not in numDict:
                return False
            numList.append(curr)
            tmp = int(tmp/10)
        
        for i in range(0, len(numList)):
            if numList[i] != numDict[numList[len(numList)-1-i]]:
                return True
        return False

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charDict = {}
        charDict['b'] = 0
        charDict['a'] = 0
        charDict['l'] = 0
        charDict['o'] = 0
        charDict['n'] = 0

        for c in text:
            if c not in charDict:
                continue
            else:
                charDict[c] +=1
        minValue = 1000
        for key, value in charDict.items():
            if key == 'l' or key == 'o':
                minValue = min(minValue, value//2)
            else:
                minValue = min(minValue, value)
        
        return minValue
        

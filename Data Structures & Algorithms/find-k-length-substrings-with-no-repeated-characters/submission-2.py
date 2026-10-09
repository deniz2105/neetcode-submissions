class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        j = k
        charDict = {}
        ssCount = 0
        if len(s) < k:
            return 0

        for i in range(j):
            if s[i] not in charDict:
                charDict[s[i]] = 1
            else:
                charDict[s[i]] += 1
        
        if len(charDict.items()) == k:
            ssCount +=1
        for i in range(k, len(s)):
            charDict[s[i-k]] -=1
            if charDict[s[i-k]] == 0:
                del charDict[s[i-k]]
            if s[i] not in charDict:
                charDict[s[i]] = 1
            else:
                charDict[s[i]] += 1
            if len(charDict.items()) == k:
                ssCount +=1
        return ssCount

        


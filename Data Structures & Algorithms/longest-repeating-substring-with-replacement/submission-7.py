class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j = 0
        charDict = {}
        maxCharCount = 0
        maxCount = 0
        for i in range(len(s)):
            if s[i] not in charDict:
                charDict[s[i]] = 1
            else:
                charDict[s[i]] += 1
            if charDict[s[i]] > maxCharCount:
                maxCharCount = charDict[s[i]] 
            while i - j +1 > maxCharCount + k:
                charDict[s[j]] -=1
                if charDict[s[j]] == 0:
                    del charDict[s[j]]
                j+=1
            
            maxCount = max(maxCount, i - j +1)
        return maxCount
            

            


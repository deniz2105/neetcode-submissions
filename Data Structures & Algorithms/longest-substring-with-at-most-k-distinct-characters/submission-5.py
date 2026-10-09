class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        charDict = {}
        if k == 0:
            return 0
        j = 0
        charDict[s[j]] = 1
        maxSize = 1
        for i in range(1,len(s)):
            if s[i] in charDict:
                charDict[s[i]] +=1
            else:
                charDict[s[i]] =1
            while j <= i and len(charDict.items()) > k:
                charDict[s[j]] -=1
                if charDict[s[j]] == 0:
                    del charDict[s[j]]
                j+=1
            maxSize = max(maxSize, i - j +1)
        
        return maxSize
            

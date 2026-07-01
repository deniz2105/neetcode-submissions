class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        charDict = {}
        maxDistinct = 0

        slowPointer = 0
        if k == 0:
            return 0
        for fastPointer in range(len(s)):
            if s[fastPointer] not in charDict:
                charDict[s[fastPointer]] = 1
            else:
                charDict[s[fastPointer]] += 1
            

            while slowPointer < fastPointer and len(charDict) > k:
                charDict[s[slowPointer]] -=1
                if charDict[s[slowPointer]] == 0:
                    charDict.pop(s[slowPointer], None)
                slowPointer+=1
            
            maxDistinct = max(maxDistinct, (fastPointer - slowPointer)+1)
        
        return maxDistinct

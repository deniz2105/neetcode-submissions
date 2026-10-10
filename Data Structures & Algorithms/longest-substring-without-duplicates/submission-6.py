class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sset = set()
        if len(s) == 0:
            return 0

        sset.add(s[0])
        currMax = 1
        j = 0

        for i in range(1, len(s)):
            while s[i] in sset:
                sset.remove(s[j])
                j+=1
            sset.add(s[i])
            currMax = max(currMax, i-j+1)
        
        return currMax
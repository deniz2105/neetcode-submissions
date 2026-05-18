class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        maxLen =0
        left =0
        for i in range(0, len(s)):
            while s[i] in ss:
                ss.remove(s[left])
                left +=1
            ss.add(s[i])
            if len(ss) > maxLen:
                maxLen = len(ss)
                

        return maxLen
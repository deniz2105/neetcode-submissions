class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sset = {}
        si = 0
        sset[s[si]] = 1
        maxLen = 1

        for i in range(1,len(s)):
            if s[i] in sset:
                sset[s[i]]+=1
            else:
                sset[s[i]]=1
            while i - si +1 > len(sset.items()):
                sset[s[si]] -=1
                
                if sset[s[si]] == 0:
                    del sset[s[si]]
                si+=1
            
            maxLen = max(len(sset.items()), maxLen)
        return maxLen
                
                



            


        
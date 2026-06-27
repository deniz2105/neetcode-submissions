class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        if len(s) == 0:
            return 0
        for i in range(0, len(s)):
            if s[i] != t[j]:
                continue
            else:
                if j == len(t)-1:
                    return 0
                j +=1
        
        return (len(t)) - j
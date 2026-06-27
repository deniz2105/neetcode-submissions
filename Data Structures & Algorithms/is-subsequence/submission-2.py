class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if s == "":
            return True
        for i in range(0, len(t)):
            if s[j] != t[i]:
                continue
            else:
                if j == len(s)-1:
                    return True
                j+=1
        return False
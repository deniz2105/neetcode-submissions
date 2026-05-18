class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                idx = t.find(c)
                t = t[:idx] + t[idx+1:]
                continue
            else:
                return False
        return t == ""
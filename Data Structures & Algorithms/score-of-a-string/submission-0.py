class Solution:
    def scoreOfString(self, s: str) -> int:
        sl = list(s)
        print(sl)
        total = 0
        for i in range(0, len(s)-1):
            total += abs(ord(sl[i]) - ord(sl[i+1]))
        return total
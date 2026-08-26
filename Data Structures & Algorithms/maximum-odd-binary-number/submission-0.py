class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count0s = 0
        count1s = 0

        for c in s:
            if c == '0':
                count0s += 1
            else:
                count1s += 1
        resp = ""
        for i in range(count1s-1):
            resp += "1"
        
        for i in range(count0s):
            resp += "0"
        
        return resp+"1"
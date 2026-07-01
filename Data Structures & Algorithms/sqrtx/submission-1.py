class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        curr = (lo + hi) // 2
        while lo <= hi:
            currsq = curr * curr
            if currsq == x:
                return curr
            elif currsq > x:
                hi = curr-1
            elif currsq < x:
                lo = curr +1
            curr = (lo + hi) // 2
        
        return curr

            
class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 1
        steps = 0
        while n > 0:
            n -= count
            count +=1
            if n >= 0:
                steps += 1
        return steps

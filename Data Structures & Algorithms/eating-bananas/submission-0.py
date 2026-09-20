class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hi = max(piles)

        lo = 1

        currBest = float('inf')
        while lo <= hi:
            curr = (lo+hi)//2
            currSum = 0
            for i in range(len(piles)):
                currSum += math.ceil(piles[i]/curr)
            if currSum <= h:
                currBest = min(currBest, curr)
                hi = curr-1
            else:
                lo = curr+1
        
        return currBest


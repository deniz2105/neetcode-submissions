class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(rate):
            totalHours = 0
            for i in range(len(piles)):
                totalHours += piles[i] // rate
                if piles[i]%rate > 0:
                    totalHours +=1
            
            return totalHours <= h
        

        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = (lo + hi)//2

            if canEat(mid):
                hi = mid
            else:
                lo = mid +1
        
        return hi
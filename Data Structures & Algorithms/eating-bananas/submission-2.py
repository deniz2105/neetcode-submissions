class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        lo = 1
        hi = max(piles)
        lastDoable = -1
        while lo <= hi:
            mid = (lo + hi)//2
            hours = 0
            doable = True
            for i in range(len(piles)):
                hours += piles[i] // mid
                if piles[i] % mid > 0:
                    hours +=1
            if hours > h:
                doable= False
            if doable:
                lastDoable = mid
                hi = mid -1
            else:
                lo = mid+1
        return lastDoable


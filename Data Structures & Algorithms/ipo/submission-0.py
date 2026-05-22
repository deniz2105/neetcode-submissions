class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profitsH = []

        for i in range(0, len(profits)):
            profitsH.append([-profits[i], i])
        
        heapq.heapify(profitsH)
        for i in range(0,k):
            popped = []
            while len(profitsH) > 0:
                curr = heapq.heappop(profitsH)
                if capital[curr[1]] <= w:
                    w+= (-curr[0])
                    break
                else:
                    popped.append(curr)
            for p in popped:
                heapq.heappush(profitsH, p)
        
        return w

class Solution:
    def jump(self, nums: List[int]) -> int:
        pq = []
        if len(nums) == 1:
            return 0
        
        heapq.heappush(pq,(-nums[0],0, 1))
        while len(pq) >0:
            currMaxIdx,currIdx, currJumps = heapq.heappop(pq)
            currMaxIdx *= -1
            if currMaxIdx >= len(nums)-1:
                return currJumps
            for i in range(currIdx+1, currMaxIdx+1):
                heapq.heappush(pq, (-nums[i]-i, i, currJumps+1))
        
        return 0


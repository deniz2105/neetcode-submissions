class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        if len(nums) <k:
            return []
        for i in range(0, k):
            heapq.heappush(pq, (-nums[i], i))
        resp=[]
        resp.append(-pq[0][0])
        for i in range(k, len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            while pq[0][1] <= i-k:
                heapq.heappop(pq)
            
            resp.append(-pq[0][0])
        return resp







    

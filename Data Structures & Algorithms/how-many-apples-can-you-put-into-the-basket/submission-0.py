class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        pq = []
        currWeight = 0

        for i in range(len(weight)):
            heapq.heappush(pq, -weight[i])
            currWeight += weight[i]
            while currWeight > 5000:
                currWeight += heapq.heappop(pq)
            
        return len(pq)


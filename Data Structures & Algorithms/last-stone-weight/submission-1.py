class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(0,len(stones)):
            stones[i] *=-1
        heapq.heapify(stones)

        while len(stones) > 1:
            num1 = -heapq.heappop(stones)
            num2 = -heapq.heappop(stones)
            heapq.heappush(stones, -(num1-num2))
        if len(stones) == 1:
            return -stones[0]
        return 0




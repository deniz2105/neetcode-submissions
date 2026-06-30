class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)

        for i in range(k):
            curr = heapq.heappop(gifts)
            curr =int((-curr) ** (1/2))
            heapq.heappush(gifts, -curr)
        
        total = 0
        for i in range(len(gifts)):
            total -= gifts[i]
        return total
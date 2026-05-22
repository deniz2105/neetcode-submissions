class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        curr = money
        heapq.heapify(prices)
        for i in range(2):
            curr -= heapq.heappop(prices)

        if curr < 0:
            return money
        else:
            return curr

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numsCopy = nums[:]
        heapq.heapify(self.numsCopy)
        self.k = k
        while len(self.numsCopy) > self.k:
            heapq.heappop(self.numsCopy)


    def add(self, val: int) -> int:
        heapq.heappush(self.numsCopy, val)

        while len(self.numsCopy) > self.k:
            heapq.heappop(self.numsCopy)
        return self.numsCopy[0]



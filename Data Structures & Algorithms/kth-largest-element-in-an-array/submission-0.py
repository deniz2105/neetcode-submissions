class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range (0, len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        curr = 0
        for i in range(0, k):
            curr = -heapq.heappop(nums)
        return curr
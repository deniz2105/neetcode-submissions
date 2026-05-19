class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentMax = nums[0]
        globalMax = nums[0]

        for i in range(1, len(nums)):
            currentMax = max(nums[i], currentMax+nums[i])
            globalMax = max(globalMax, currentMax)
        return globalMax
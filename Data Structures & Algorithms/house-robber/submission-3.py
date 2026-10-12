class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxPayout = [0]*len(nums)
        maxPayout[0] = nums[0]
        if len(nums)==1:
            return nums[0]
        maxPayout[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            maxPayout[i] = max(maxPayout[i-1], nums[i]+maxPayout[i-2])
        
        return maxPayout[-1]
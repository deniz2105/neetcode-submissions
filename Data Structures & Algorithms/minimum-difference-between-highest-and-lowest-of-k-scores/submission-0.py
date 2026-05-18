class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        diff = nums[k-1] - nums[0]
        for i in range(k, len(nums)):
            if (nums[i] - nums[i-k+1]) < diff:
                diff = (nums[i] - nums[i-k+1])
        
        return diff



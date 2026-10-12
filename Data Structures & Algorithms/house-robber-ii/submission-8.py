class Solution:
    def rob(self, nums: List[int]) -> int:
        lMax = [0]*(len(nums)-1)
        sMax = [0] * (len(nums)-1)
        if len(nums) == 1:
            return nums[0]
        lMax[0] = nums[-1]
        sMax[0] = nums[0]

        if len(nums) == 2:
            return max(nums[-1], nums[0])

        lMax[1] = max(nums[-1], nums[0])
        sMax[1] = max(nums[1], nums[0])
        print(lMax)
        print(sMax)
        for i in range(2, len(nums)-1):
            lMax[i] = max(lMax[i-1], lMax[i-2]+nums[i-1])
            sMax[i] = max(sMax[i-1], sMax[i-2]+nums[i])
        
        return max(lMax[-1], sMax[-1])
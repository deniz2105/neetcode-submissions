class Solution:
    def rob(self, nums: List[int]) -> int:
        maxMoney = []

        maxMoney.append(nums[0])
        if len(nums) == 1:
            return maxMoney[0]
        maxMoney.append(max(nums[1], nums[0]))

        for i in range(2, len(nums)):
            maxMoney.append(max(nums[i]+maxMoney[i-2], maxMoney[i-1]))
        
        return maxMoney[-1]
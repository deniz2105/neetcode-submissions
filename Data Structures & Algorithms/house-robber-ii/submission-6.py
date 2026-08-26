class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return nums[0]

        def robHelper(nums: List[int]) -> int:
            maxMoney = []
            maxMoney.append(nums[0])

            if len(nums) == 1:
                return maxMoney[0]
            
            maxMoney.append(max(nums[0], nums[1]))
            if len(nums) == 2:
                return maxMoney[-1]
            for i in range(2, len(nums)):
                maxMoney.append(max(nums[i] + maxMoney[i-2], maxMoney[i-1]))
            print(maxMoney)
            return maxMoney[-1]
        
        return max(robHelper(nums[1:]), robHelper(nums[:-1]))

        
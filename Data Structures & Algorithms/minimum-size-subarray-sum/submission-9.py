class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0

        currSum = nums[0]

        if currSum >= target:
            return 1
        minLength = len(nums)
        for right in range(1, len(nums)):
            currSum += nums[right]

            while currSum - nums[left] >= target:
                currSum -= nums[left]
                left +=1
                if len(nums[left:right+1]) < minLength:
                    minLength = len(nums[left:right+1])
        right = len(nums)-1
        while currSum - nums[right] >= target and right > left:
                currSum -= nums[right]
                right -=1
                if len(nums[left:right+1]) < minLength:
                    minLength = len(nums[left:right+1])
        if currSum >= target:
            return minLength 
        return 0
        


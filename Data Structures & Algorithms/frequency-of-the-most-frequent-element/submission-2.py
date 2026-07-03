class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)

        slowPointer = 0
        currSum = nums[slowPointer]
        currSumReal = nums[slowPointer]
        maxLen = 1

        for i in range(1, len(nums)):
            currSum += nums[slowPointer]
            currSumReal += nums[i]
            while currSum - currSumReal > k:
                diff = nums[slowPointer] - nums[slowPointer+1]
                currSumReal -= nums[slowPointer]
                slowPointer+=1
                currSum = nums[slowPointer] * (i - slowPointer+1)
            print(maxLen)
            maxLen = max(i - slowPointer+1, maxLen)
        return maxLen
                



            
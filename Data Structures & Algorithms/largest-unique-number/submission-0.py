class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] not in numsDict:
                numsDict[nums[i]] = 1
            else:
                numsDict[nums[i]] = numsDict[nums[i]] + 1
        
        maxNum = -1
        for i in range(len(nums)):
            if numsDict[nums[i]] == 1:
                maxNum = max(maxNum, nums[i])
        return maxNum

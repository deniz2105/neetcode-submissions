class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numsDict = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in numsDict:
                numsDict[nums[i]] = 1
            else:
                numsDict[nums[i]] += 1
                count +=numsDict[nums[i]]-1
        return count
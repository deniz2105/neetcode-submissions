class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numDict = {}
        for i in range(0, len(nums)):
            if nums[i] not in numDict:
                numDict[nums[i]] = 1
            else:
                numDict[nums[i]] += 1

        for i in range(0, len(nums)):
            if numDict[nums[i]] % 2 != 0:
                return False
        

        return True


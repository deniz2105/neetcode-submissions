class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isIncreasing = False
        isDecreasing = False

        maxDiffGrtr0 = False
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            if nums[i] > nums[i+1]:
                if isIncreasing:
                    return False
                isDecreasing = True
            if nums[i] < nums[i+1]:
                if isDecreasing:
                    return False
                isIncreasing = True
        return True
            

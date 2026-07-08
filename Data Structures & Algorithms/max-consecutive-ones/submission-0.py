class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1s = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max1s = max(max1s, curr)
                curr = 0
            else:
                curr +=1
        
        max1s = max(max1s, curr)
        return max1s        

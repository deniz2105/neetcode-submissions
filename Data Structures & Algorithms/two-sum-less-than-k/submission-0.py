class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        maxVal = -1
        left = 0
        right = len(nums)-1
        nums.sort()
        while left < right:
            if (nums[left] + nums[right]) < k:
                maxVal = max((nums[left] + nums[right]), maxVal)
                left +=1
            else:
                right -=1
        return maxVal
            

            




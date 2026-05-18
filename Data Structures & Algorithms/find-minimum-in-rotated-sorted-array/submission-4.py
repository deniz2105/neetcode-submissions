class Solution:
    def findMin(self, nums: List[int]) -> int:
        hi = len(nums)-1
        lo = 0
        firstVal = nums[0]
        if nums[hi] >= nums[lo]:
            return nums[lo]
        while hi >= lo:
            mid = (hi + lo)//2
            if mid > 0 and nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] >= firstVal:
                lo = mid +1
            else:
                hi = mid-1
        return -1

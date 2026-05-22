class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1
        
        while lo <= hi:
            mid = (lo + hi)//2

            if nums[mid] == target:
                return mid

            leftSorted = nums[mid] > nums[lo]
            rightSorted = nums[mid] < nums[hi]

            if nums[mid] > target >= nums[lo]:
                hi = mid-1
            elif nums[hi] >= target > nums[mid]:
                lo = mid + 1
            elif nums[hi] < nums[mid]:
                lo = mid + 1
            else:
                hi = mid-1
        
        return -1


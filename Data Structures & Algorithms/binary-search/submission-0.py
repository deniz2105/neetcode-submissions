class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        hi = len(nums)-1

        while low <= hi:
            i = (low + hi)//2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                hi = i-1
            else:
                low = i+1
        
        return -1
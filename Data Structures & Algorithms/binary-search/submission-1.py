class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            curr = (lo + hi)//2

            if nums[curr] == target:
                return curr
            elif nums[curr] > target:
                hi = curr-1
            else:
                lo = curr+1
        return -1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            i = (lo + hi) //2
            
            if nums[i] == target:
                return i
            
            if nums[i] > target:
                hi = i -1
                print("hi")
                print(hi)
            else:
                lo = i + 1
                print("lo")
                print(lo)
        
        return lo

            

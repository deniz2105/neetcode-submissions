class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot = -1
        lo = 0
        hi = len(nums)-1
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if (nums[0] == target): 
                return 0 
            else: 
                return -1
        if nums[lo] < nums[hi]:
            pivot = 0
        else:
            while lo <= hi:
                curr = (lo+hi)//2
                if curr == len(nums) -1 and nums[curr] > nums[0]:
                    pivot = 0
                    break
                if nums[curr] > nums[curr+1]:
                    
                    pivot = curr+1
                    break
                elif nums[lo] <= nums[curr]:
                    lo = curr+1
                else:
                    hi = curr -1
        print(pivot)
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            curr = (lo + hi) //2
            tCurr = (curr + pivot) % len(nums)
            
            if nums[tCurr] == target:
                return tCurr
            elif nums[tCurr] > target:
                hi = curr-1
            else:
                lo = curr+1
        return -1






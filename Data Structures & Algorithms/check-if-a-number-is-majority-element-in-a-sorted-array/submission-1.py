class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        lo = 0
        hi = len(nums)-1
        currLowest = -1

        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                currLowest = mid
                hi = mid -1
            else:
                lo = mid +1
        

        if currLowest == -1:
            return False
        print("lo")
        print(currLowest)
        majNum = (len(nums)//2)
        print("majNum")
        print(majNum)

        if currLowest + majNum >= len(nums):
            return False
        return nums[currLowest + majNum] == target






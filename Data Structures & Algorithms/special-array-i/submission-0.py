class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        curr = (nums[0] %2 ==0)
        for i in range(1, len(nums)-1):
            if ((nums[i] %2 ==0) ^ curr) == False:
                return False
            curr = (nums[i] %2 ==0)
        return True


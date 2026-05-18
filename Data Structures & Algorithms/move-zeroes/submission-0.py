class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = []
        for i in range(0, len(nums)):
            if nums[i]!= 0:
                tmp.append(nums[i])
        
        for i in range(0, len(nums)):
            if i < len(tmp):
                nums[i] = tmp[i]
            else:
                nums[i] = 0
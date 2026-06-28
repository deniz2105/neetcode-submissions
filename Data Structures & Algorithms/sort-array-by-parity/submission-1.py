class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        tmp = -1
        j = len(nums)
        i = 0
        while i < j:
            if nums[i] % 2 == 0:
                i+=1
                continue
            tmp = nums[i]
            nums.pop(i)
            nums.append(tmp)
            j -=1
        return nums


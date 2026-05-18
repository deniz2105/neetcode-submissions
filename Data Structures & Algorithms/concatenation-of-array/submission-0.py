class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2n = [0 for i in range(len(nums)*2)]
        for i in range(len(nums)*2):
            nums2n[i] = nums[i%(len(nums))]
        return nums2n
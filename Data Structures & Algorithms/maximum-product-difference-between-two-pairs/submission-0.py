class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s = sorted(nums)

        mins = s[0:2]
        maxs = s[len(s)-2:len(s)]

        return (maxs[0]*maxs[1]) - (mins[0]*mins[1])

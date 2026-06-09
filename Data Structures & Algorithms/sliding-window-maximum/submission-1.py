class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k-1
        maxs = []
        while right < len(nums):
            window = sorted(nums[left:right+1])
            maxs.append(window[k-1])
            left+=1
            right +=1
        return maxs

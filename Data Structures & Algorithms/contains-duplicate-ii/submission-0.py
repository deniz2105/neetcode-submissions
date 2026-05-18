class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        right = 1
        for left in range(0, len(nums)):
            right = left +1
            while left<right and (right-left) <= k and right < len(nums):
                if nums[left] == nums[right]:
                    return True
                right+=1

        return False

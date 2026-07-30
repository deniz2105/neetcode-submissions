class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = nums[left]
        count = 0
        if product < k:
            count +=1
        for right in range(1, len(nums)):
            product = product * nums[right]
            
            while product >= k and left <= right:
                product = product // nums[left]
                left +=1
            if product < k:
                count += (right - left)+1
            
        return count


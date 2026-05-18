class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = nums[0]
        for i in range(1, len(nums)):
            if maxJump < i:
                break
            if i == maxJump or maxJump < nums[i]+i:
                maxJump = nums[i]+i
            print(maxJump)
        return maxJump >= len(nums)-1
            

                

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        newList = []

        while left <= right:
            leftSqrd = nums[left]**2
            rightSqrd = nums[right]**2
            if leftSqrd > rightSqrd:
                newList.append(leftSqrd)
                left+=1
            else:
                newList.append(rightSqrd)
                right-=1

        return newList[::-1]
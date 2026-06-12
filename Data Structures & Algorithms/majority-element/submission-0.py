class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currElement = -1000000001
        count = 0

        for i in range(0, len(nums)):
            if nums[i] == currElement:
                count +=1
            else:
                if count - 1 <= 0:
                    currElement = nums[i]
                    count =1
                else:
                    count -=1
        
        return currElement

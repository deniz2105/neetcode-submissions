class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        slowPointer = 0
        fastPointer = 0
        zeroes = 0
        ones = 0
        globalMax = 0
        while fastPointer < len(nums):
            if nums[fastPointer] == 1:
                ones +=1
                fastPointer +=1
            else:
                zeroes+=1
                fastPointer +=1
            if zeroes >1:
                while slowPointer < fastPointer and zeroes > 1:
                    if nums[slowPointer] == 0:
                        zeroes -=1
                    else:
                        ones -=1
                    slowPointer +=1
            else:
                globalMax = max(globalMax, ones+zeroes)
        return globalMax

        

        



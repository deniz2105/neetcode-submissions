class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #redo this
        rangeD = {}
        ptr = 2 ** 31
        inBetweenVal = float('inf')
        rangeD[ptr] = -1
        for i in range(len(nums)):
            if nums[i] == inBetweenVal:
                inBetweenVal = float('inf')
            if nums[i] < 1:
                continue
            elif nums[i] < ptr:
                if ptr - nums[i] != 1 and inBetweenVal > nums[i]+1:
                    inBetweenVal = nums[i]+1
                val = rangeD.pop(ptr)
                ptr = nums[i]
                rangeD[ptr] = val
            elif rangeD[ptr] < nums[i]:
                if rangeD[ptr] != -1 and nums[i]-rangeD[ptr] != 1 and inBetweenVal > nums[i]-1:
                    inBetweenVal = rangeD[ptr]+1
                rangeD[ptr] = nums[i]

        if ptr > 1:
            return 1
        elif inBetweenVal != float('inf'):
            return inBetweenVal
        else: 
            return rangeD[ptr] +1

            
                
        


        
            


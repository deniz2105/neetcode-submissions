class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLongest = 1
        localLongest = 1
        cons = {}
        if len(nums) == 0:
            return 0

        cons[nums[0]] = [None, None]
        for i in range(1, len(nums)):
            if nums[i] not in cons:
                cons[nums[i]] = [None, None]
                if nums[i] -1 in cons:
                    cons[nums[i]-1][1] = nums[i]
                    cons[nums[i]][0] = nums[i]-1
                if nums[i] +1 in cons:
                    cons[nums[i]+1][0] = nums[i]
                    cons[nums[i]][1] = nums[i]+1
        
        for key, value in cons.items():
            node = None
            if value[0] == None and value[1] != None:
                localLongest +=1
                curr = value[1]
                while cons[curr][1] != None:
                    localLongest +=1
                    curr = cons[curr][1]
                if localLongest > maxLongest:
                    maxLongest = localLongest
            localLongest = 1
        
        return maxLongest
        

        
                    


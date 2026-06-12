class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        curr1 = -1000000001
        
        curr2 = -1000000001
        count1 = 0
        count2 = 0

        for i in range(0, len(nums)):
            if nums[i] == curr1:
                count1 +=1
                continue
            elif nums[i] == curr2:
                count2 +=1
                continue

                
            

            if count1 < 1:
                curr1 = nums[i]
                count1 = 1
                continue
            elif count2 < 1:
                curr2 = nums[i]
                count2 = 1
                continue
            count1 -=1
            count2 -=1

        
        resp = []
        realCount1 = 0
        realCount2 = 0
        for i in range(0, len(nums)):
            if curr1 == nums[i]:
                realCount1 +=1
            elif curr2 == nums[i]:
                realCount2 +=1
        if realCount1 > len(nums)/3:
            resp.append(curr1)

        if realCount2 > len(nums)/3 and curr1 != curr2:
            resp.append(curr2)

        return resp

        
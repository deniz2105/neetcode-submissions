class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-1,0,1,2,-1,-4]
        nums.sort()
        #[-4,-1,-1,0,1,2]
        triplets = set()
        for i in range(len(nums)):
            left = i+1
            right = (len(nums)-1)
            while right > left:
                summed = nums[i] + nums[left] + nums[right]
                if summed > 0:
                    right -= 1
                elif summed < 0:
                    left += 1
                else:
                    triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
        return list(triplets)
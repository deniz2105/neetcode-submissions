class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        counter = 0
        nums.sort()
        for i in range(len(nums)-2):

            curr = nums[i]
            l = i+1
            r = len(nums)-1
            while l < r:
                if curr + nums[l] + nums[r] >= target:
                    r-=1
                else:
                    counter +=(r-l)
                    l+=1
        return counter


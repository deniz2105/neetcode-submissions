class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sset = set()
        for i in range(len(nums)):
            sset.add(nums[i])
        setList = list(sset)
        setList.sort()
        for i in range(len(setList)):
            nums[i] = setList[i]
        
        return len(sset)




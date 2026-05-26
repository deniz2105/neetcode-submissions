class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def decide(nums: list[int], idx: int, prevSubset: list[int]) -> list[list[int]]:
            newSubset = prevSubset[:]
            newSubset.append(nums[idx])
            if idx == len(nums)-1:
                return [newSubset, prevSubset]
            currList = []
            currList.extend(decide(nums, idx+1, newSubset))
            currList.extend(decide(nums, idx+1, prevSubset))
            return currList
        return decide(nums, 0,[])

            

            


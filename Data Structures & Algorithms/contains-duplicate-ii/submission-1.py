class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nset = set()
        nset.add(nums[0])
        for i in range(1, len(nums)):
            if i-k > 0:
                nset.remove(nums[i-k-1])
            if nums[i] in nset:
                return True
            nset.add(nums[i])
        return False

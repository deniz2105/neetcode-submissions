class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numsDict = {}
        for i in range(len(nums1)):
            numsDict[nums1[i]] = -1
        for i in range(len(nums2)):
            if numsDict[nums2[i]] == -1:
                numsDict[nums2[i]] = i
        idxs = []
        for i in range(len(nums1)):
            idxs.append(numsDict[nums1[i]])
        return idxs


        

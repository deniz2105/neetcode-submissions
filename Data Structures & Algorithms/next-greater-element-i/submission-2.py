class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Idx = {}
        for i in range(len(nums2)-1, -1, -1):
            if i == len(nums2)-1:
                nums2Idx[nums2[i]] = [i,-1]
            else:
                j = i+1
                nextGreater = -1
                while j < len(nums2):
                    if nums2[j] > nums2[i]:
                        nextGreater = nums2[j]
                        break
                    j+=1
                    
                nums2Idx[nums2[i]] = [i,nextGreater]
        result = []
        for i in range(len(nums1)):
            idx = nums2Idx[nums1[i]][0]
            if idx == len(nums2)-1:
                result.append(-1)
            elif nums1[i] < nums2Idx[nums1[i]][1]:
                result.append(nums2Idx[nums1[i]][1])
            else:
                result.append(-1)
        return result
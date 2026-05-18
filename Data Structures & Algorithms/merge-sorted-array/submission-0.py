class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        def shiftInsert(val: int, idx: int, nums: List[int]):
            for i in range (len(nums)-2, idx-1, -1):
                nums[i+1] = nums[i]
            nums[idx] = val

        while p2 < n:
            if p1 >= m + p2 or nums1[p1] >= nums2[p2]:
                print(nums1)
                shiftInsert(nums2[p2], p1, nums1) 
                print("indexes")
                print("p1")
                print(p1)
                print("p2")
                print(p2)
                p2 += 1
                p1 += 1
            else:
                p1 +=1
        


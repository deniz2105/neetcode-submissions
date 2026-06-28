class Solution:
    def countElements(self, arr: List[int]) -> int:
        numsDict = {}
        for i in range(len(arr)):
            numsDict[arr[i]] = True
        count = 0
        for i in range(len(arr)):
            if arr[i]+1 in numsDict:
                count+=1
        return count

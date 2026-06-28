class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            arr[i] *=-1
        
        newArr = []
        for i in range(len(arr)-1):
            rightSide = arr[i+1:len(arr)]
            heapq.heapify(rightSide)
            newArr.append(-heapq.heappop(rightSide))
        newArr.append(-1)
        return newArr

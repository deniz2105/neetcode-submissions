class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        maxDiff = 0
        missingIdx = 0
        for i in range(len(arr)-1):
            if maxDiff < abs(arr[i+1] - arr[i]):
                maxDiff = abs(arr[i+1] - arr[i])
                missingIdx = i

        if arr[0] > arr[len(arr)-1]:
            maxDiff = -maxDiff
        
        return arr[missingIdx] + (maxDiff//2)
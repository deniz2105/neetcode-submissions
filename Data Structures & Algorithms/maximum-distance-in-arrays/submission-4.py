class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        globalMax = arrays[0][len(arrays[0])-1]
        globalMin = arrays[0][0]
        maxDiff = 0

        for i in range(1, len(arrays)):
            if abs(arrays[i][len(arrays[i])-1] - globalMin) > maxDiff:
                maxDiff = abs(arrays[i][len(arrays[i])-1] - globalMin)
                
                
                print(maxDiff)
            if abs(arrays[i][0] - globalMax) > maxDiff:
                print(arrays[i][0])
                print(globalMax)
                maxDiff = abs(arrays[i][0] - globalMax) 
                print(maxDiff)
            
            globalMax = max(arrays[i][len(arrays[i])-1], globalMax)
            globalMin = min(arrays[i][0], globalMin)
        
        return maxDiff
                



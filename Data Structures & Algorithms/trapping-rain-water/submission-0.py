class Solution:
    def trap(self, height: List[int]) -> int:
        rightWalls = [0 for i in range(0,len(height))]
        leftWalls = [0 for i in range(0,len(height))]
        for i in (range(1,len(height))):
            leftWalls[i] = max(leftWalls[i-1], height[i-1])
        for i in (range(len(height)-2, -1, -1)):
            rightWalls[i] = max(rightWalls[i+1], height[i+1])
        
        waterVolume = 0
        for i in (range(0,len(height))):
            waterVolume += max(0, (min(leftWalls[i], rightWalls[i])-height[i]))
        return waterVolume
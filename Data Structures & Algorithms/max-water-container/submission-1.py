class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = 0
        while left < right:
            width = right-left
            area = min(heights[left], heights[right]) * width
            print("min h")
            print(min(heights[left], heights[right]))
            print("width")
            print(width)
            print("left")
            print(left)
            print("right")
            print(right)
            if maxArea < area:
                maxArea = area
            
            if heights[left] > heights[right]:
                right -=1
            else:
                left +=1
        return maxArea

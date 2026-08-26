class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        resp = []
        resp.append(len(heights)-1)
        maxHeight = heights[-1]

        for i in range(len(heights)-2, -1, -1):
            if heights[i]> maxHeight:
                resp.insert(0, i)
                maxHeight = heights[i]
        
        return resp

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d2o = []
        for i in range(0, len(points)):
            dist = (points[i][0]**2 + points[i][1]**2)**0.5
            distIdx = [dist, i]
            d2o.append(distIdx)
        
        heapq.heapify(d2o)
        firstK = []
        for i in range(0,k):
            curr = heapq.heappop(d2o)
            firstK.append(points[curr[1]])
        return firstK
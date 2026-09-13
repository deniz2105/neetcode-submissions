class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:(x[1], -x[0]))
        print(intervals)
        toRemove = 0
        resp = []
        for i in range(len(intervals)):
            if resp and intervals[i][0]<resp[-1][1]:
                toRemove+=1
            else:
                resp.append(intervals[i])
        
        return toRemove
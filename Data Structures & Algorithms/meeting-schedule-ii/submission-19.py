"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key= lambda x:x.start)

        pq = []
        heapq.heappush(pq, (intervals[0].end, 0))
        maxLen = 1
        for i in range(1, len(intervals)):
            while len(pq) > 0 and pq[0][0] <= intervals[i].start:
                heapq.heappop(pq)
            
            heapq.heappush(pq, (intervals[i].end, i))
            maxLen= max(maxLen, len(pq))
        
        return maxLen

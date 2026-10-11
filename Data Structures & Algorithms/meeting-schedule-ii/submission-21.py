"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)

        pq = []
        maxSize = 0

        for i in range(len(intervals)):
            while len(pq) >0 and pq[0] <= intervals[i].start:
                heapq.heappop(pq)
            
            heapq.heappush(pq, intervals[i].end)
            maxSize = max(maxSize, len(pq))
        
        return maxSize
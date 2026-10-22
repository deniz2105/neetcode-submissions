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

        if len(intervals) == 0:
            return 0

        maxRooms = 0
        pq = []

        for i in intervals:
            while len(pq)>0 and i.start >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq,i.end)
            maxRooms = max(maxRooms, len(pq))
        return maxRooms
        

                
        
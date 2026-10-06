"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x:x.start)
        resp = []

        for i in range(len(intervals)):
            if len(resp) == 0 or not (resp[-1].start < intervals[i].end and intervals[i].start < resp[-1].end):
                resp.append(intervals[i])
            else:
                return False
        return True
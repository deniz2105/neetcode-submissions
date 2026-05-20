"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #intervals.sort()
        intervalsArr = []
        for i in range(len(intervals)):
            intervalsArr.append([intervals[i].start, intervals[i].end])
        intervalsArr.sort()
        for i in range(0, len(intervals)-1):
            if intervalsArr[i][1] > intervalsArr[i+1][0]:
                return False
        return True

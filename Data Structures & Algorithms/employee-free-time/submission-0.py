"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        employeeBusyTimes = []
        pq = []

        for i, s in enumerate(schedule):
            heapq.heappush(pq, (s[0].start,s[0].end, i, 0))
        
        busy = []
        while len(pq) > 0:
            start,end, employeeId, slotId = heapq.heappop(pq)
            if len(schedule[employeeId]) > slotId +1:
                heapq.heappush(pq, (schedule[employeeId][slotId +1].start, schedule[employeeId][slotId +1].end, employeeId, slotId +1))
            if len(busy) == 0 or busy[-1].end < start:
                busy.append(Interval(start,end))
            else:
                busy[-1].start = min(busy[-1].start, start)
                busy[-1].end = max(busy[-1].end, end)
        
        start = float('-inf')
        end = busy[0].start
        free = []
        for i in range(0,len(busy)):
            print("start"+str(busy[i].start)+"end"+str(busy[i].end))
        for i in range(1,len(busy)):
            start = busy[i-1].end
            end = busy[i].start
            free.append(Interval(start, end))
        return free

        








     
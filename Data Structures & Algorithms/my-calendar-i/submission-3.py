import bisect
class MyCalendar:
    
    def __init__(self):
        self.startTimes = []
        self.endTimes = []

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect.bisect_right(self.startTimes, startTime)

        if idx < len(self.startTimes) and max(self.startTimes[idx], startTime) < min(self.endTimes[idx], endTime):
            return False
        if idx-1 >= 0 and max(self.startTimes[idx-1], startTime) < min(self.endTimes[idx-1], endTime):
            return False
        self.startTimes.insert(idx, startTime)
        self.endTimes.insert(idx, endTime)
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
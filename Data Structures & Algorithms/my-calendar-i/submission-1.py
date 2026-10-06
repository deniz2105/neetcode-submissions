import bisect
class MyCalendar:
    
    def __init__(self):
        self.meetingStarts = []
        self.meetingEnds = []

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.meetingStarts) == 0:
            self.meetingStarts.append(startTime)
            self.meetingEnds.append(endTime)
            return True
        idx = bisect.bisect_right(self.meetingStarts, startTime)
        if idx >0 and (self.meetingStarts[idx-1] < endTime and startTime < self.meetingEnds[idx-1]):
            print(self.meetingStarts)
            print(self.meetingEnds)
            return False
        
        if idx < len(self.meetingStarts) and (self.meetingStarts[idx] < endTime and startTime < self.meetingEnds[idx]):
            print(self.meetingStarts)
            print(self.meetingEnds)
            return False
        
        self.meetingStarts.insert(idx, startTime)
        self.meetingEnds.insert(idx, endTime)

        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
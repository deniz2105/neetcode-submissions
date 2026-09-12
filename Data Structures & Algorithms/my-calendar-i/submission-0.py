import bisect

class MyCalendar:
    
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        for i in range(len(self.events)):
            if self.events[i][0] < endTime and startTime < self.events[i][1]:
                return False
            
        self.events.append([startTime, endTime])
        return True
        


# param_1 = obj.book(startTime,endTime)
import bisect
class TimeMap:

    def __init__(self):
        self.tDict = {}
        self.vDict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tDict:
            self.tDict[key] = [timestamp]
            self.vDict[key] = [value]
        else:
            self.tDict[key].append(timestamp)
            self.vDict[key].append(value)



    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tDict:
            return ""
        if timestamp <self.tDict[key][0]:
            return ""
        idx = bisect.bisect_left(self.tDict[key], timestamp)
        if len(self.tDict[key]) <= idx or self.tDict[key][idx] > timestamp:
            idx-=1


        
        return self.vDict[key][idx]

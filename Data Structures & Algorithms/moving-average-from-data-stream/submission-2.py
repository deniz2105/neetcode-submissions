class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = []
        self.currSum = 0

    def next(self, val: int) -> float:
        if len(self.arr) == self.size:
            self.currSum -= self.arr.pop(0)
        self.currSum += val
        self.arr.append(val)
        
        return self.currSum/len(self.arr)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

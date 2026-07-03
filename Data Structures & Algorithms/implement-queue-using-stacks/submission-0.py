class MyQueue:

    def __init__(self):
        self.s = []
        self.buffer = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        while len(self.s) > 1:
            self.buffer.append(self.s.pop())
        
        resp = self.s.pop()

        while len(self.buffer) > 0:
            self.s.append(self.buffer.pop())
        return resp
        

    def peek(self) -> int:
        while len(self.s) > 1:
            self.buffer.append(self.s.pop())
        
        resp = self.s.pop()
        self.buffer.append(resp)

        while len(self.buffer) > 0:
            self.s.append(self.buffer.pop())
        return resp
        

    def empty(self) -> bool:
        return len(self.s) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
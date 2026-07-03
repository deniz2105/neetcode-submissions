class MyStack:

    def __init__(self):
        self.q = deque()
        self.buffer = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        while len(self.q) > 1:
            self.buffer.append(self.q.popleft())
        resp = self.q.popleft()

        while len(self.buffer) > 0:
            self.q.append(self.buffer.popleft())
        return resp
        

    def top(self) -> int:
        while len(self.q) > 1:
            self.buffer.append(self.q.popleft())
        resp = self.q.popleft()
        while len(self.buffer) > 0:
            self.q.append(self.buffer.popleft())
        self.q.append(resp)
        return resp
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
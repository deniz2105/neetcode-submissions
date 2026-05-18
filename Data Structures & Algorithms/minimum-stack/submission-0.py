class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[len(self.minstack)-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[len(self.minstack)-1])

    def pop(self) -> None:
        self.stack = self.stack[0:len(self.stack)-1]
        self.minstack = self.minstack[0:len(self.minstack)-1]

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.minstack[len(self.minstack)-1]
        

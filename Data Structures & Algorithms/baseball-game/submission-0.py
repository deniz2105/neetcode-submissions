class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()

        for i in range(0, len(operations)):
            if operations[i] == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                stack.append(num1+num2)
            elif operations[i] == "D":
                num1 = stack[-1]
                stack.append(num1*2)
            elif operations[i] == "C":
                stack.pop()
            else:
                stack.append(int(operations[i]))
        summed = 0
        while (len(stack)!=0):
            curr = stack.pop()
            summed += curr
        return summed
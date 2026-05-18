class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def aritmethic(num1, num2, operation):
            if operation == "+":
                return num1 + num2
            elif operation == '-':
                return num1 - num2
            elif operation == '/':
                return num1/num2
            else:
                return num1* num2

        operators = {'+', '-', '*', '/'}
        stack = deque()
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                result = int(aritmethic(num1, num2, tokens[i]))
                stack.append(result)
        
        return stack.pop()


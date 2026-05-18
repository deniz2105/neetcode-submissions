class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        if len(temperatures) == 0:
            return [0]
        results = [0 for i in range(len(temperatures))]
        for i in range(0, len(temperatures)):
            if len(stack) == 0:
                stack.append(i)
            elif temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                    poppedIdx = stack[-1]
                    results[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return results



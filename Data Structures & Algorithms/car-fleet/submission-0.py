class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ttr = []
        for i in range(0, len(position)):
            ttr.append([position[i], (target - position[i]) / speed[i]])

        #if position[i] > position[j] and ttr[i] < ttr[j] -> fleet
        ttr.sort(reverse=True)
        print(ttr)
        stack = deque()
        for i in range(0, len(position)):
            if len(stack) == 0:
                stack.append(ttr[i])
            elif stack[-1][1] >= ttr[i][1]:
                ttr[i][1] = stack[-1][1]
                stack.append(ttr[i])
            else:
                stack.append(ttr[i])
        
        lastVal = -1
        numFleets = 0
        while len(stack) != 0:
            currTtr = stack.pop()[1]
            print(currTtr)
            if currTtr != lastVal:
                numFleets +=1
                lastVal = currTtr
        return numFleets

        
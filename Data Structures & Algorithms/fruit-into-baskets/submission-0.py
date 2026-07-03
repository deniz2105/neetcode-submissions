class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        slowPointer = 0
        fruitsDict = {}
        fruitsDict[fruits[slowPointer]] = 1
        maxTotal = 1
        currTotal = 1

        for i in range(1, len(fruits)):
            
            if fruits[i] not in fruitsDict:
                fruitsDict[fruits[i]] = 1
            else:
                fruitsDict[fruits[i]] += 1
            currTotal +=1
            
            while len(fruitsDict) > 2:
                currTotal -= 1
                fruitsDict[fruits[slowPointer]] -= 1
                if fruitsDict[fruits[slowPointer]] == 0:
                    fruitsDict.pop(fruits[slowPointer], None)
                slowPointer+=1
            maxTotal = max(currTotal, maxTotal)
        return maxTotal

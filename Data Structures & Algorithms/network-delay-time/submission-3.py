class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edgeDict = defaultdict(list)

        for time in times:
            edgeDict[time[0]].append((time[2], time[1]))
        
        cheapestPaths = {}
        cheapestPaths[k] = 0
        pq = []
        heapq.heappush(pq, (cheapestPaths[k], k))

        while pq:
            currCost, currNode = heapq.heappop(pq)

            if cheapestPaths[currNode] < currCost:
                continue
            
            if currNode not in edgeDict:
                continue
            for neighbor in edgeDict[currNode]:
                if neighbor[1] not in cheapestPaths or cheapestPaths[neighbor[1]] > currCost + neighbor[0]:
                    cheapestPaths[neighbor[1]] = currCost + neighbor[0]
                    heapq.heappush(pq, (cheapestPaths[neighbor[1]], neighbor[1]))
        for i in range(1,n+1):
            if i not in cheapestPaths:
                return -1
        return max(cheapestPaths.values())


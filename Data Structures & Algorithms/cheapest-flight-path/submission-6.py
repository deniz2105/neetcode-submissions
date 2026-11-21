class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flightDict = defaultdict(list)

        for flight in flights:
            flightDict[flight[0]].append((flight[2], flight[1]))
        
        pq = []

        if src not in flightDict:
            return -1
        for f in flightDict[src]:
            heapq.heappush(pq, (f[0],0, f[1]))
        
        cheapest = {}
        cheapest[(src, 0)] = 0

        while pq:
            currCost, currStops, currNode = heapq.heappop(pq)

            if currNode == dst:
                return currCost
            else:
                currStops+=1
            
            if currStops > k:
                continue
            for f in flightDict[currNode]:
                if ((f[1], currStops+1) not in cheapest or cheapest[(f[1], currStops+1)] > f[0]+ currCost) and (currStops+1 <= k or f[1] == dst):
                    heapq.heappush(pq,  (f[0]+ currCost,currStops, f[1]))
                    cheapest[(f[1], currStops+1)] = f[0]+ currCost
        return -1
            


            
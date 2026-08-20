class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort()

        resp = []
        curr = items[0][0]
        h = []
        heapq.heapify(h)
        for i in range(len(items)):
            if curr != items[i][0]:
                respI = 0
                for j in range(5):
                    respI -= heapq.heappop(h)
                resp.append([curr, respI//5])
                curr = items[i][0]
                h = []
                heapq.heapify(h)
            
            heapq.heappush(h, -items[i][1])
        respI = 0
        for j in range(5):
            respI -= heapq.heappop(h)
        resp.append([curr, respI//5])
        return resp

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqDict = {}
        for i in range(len(tasks)):
            if tasks[i] not in freqDict:
                freqDict[tasks[i]]  = 1
            else:
                freqDict[tasks[i]] += 1
        freqs = []
        for k, v in freqDict.items():
            freqs.append((-v, k))
        print(freqs)
        heapq.heapify(freqs)
        print(freqs)
        maxFreq = -freqs[0][0]
        
        maxSlots = maxFreq + n * (maxFreq-1)
        count = 0
        heapq.heappop(freqs)
        while freqs and -freqs[0][0] == maxFreq:
            count+=1
            heapq.heappop(freqs)
        
        return max(len(tasks), maxSlots + count)
        


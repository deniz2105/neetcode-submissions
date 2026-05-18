class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}

        for n in nums:
            if n not in occ:
                occ[n] = 1
            else:
                occ[n] += 1
        
        freqs = [[] for _ in range(len(nums)+1)]
        for key, value in occ.items():
            freqs[value].append(key)
        
        topK = []
        count = 0

        for i in range(len(freqs)-1, -1, -1):
            if freqs[i] != []:
                print(freqs[i])
                topK.extend(freqs[i])
                count+=(len(freqs[i]))
            if count == k:
                return topK[0:k]
        return topK
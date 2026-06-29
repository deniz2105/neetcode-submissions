class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = {}
        for i in range(len(s)):
            if s[i] not in freqs:
                freqs[s[i]] = 1
            else:
                freqs[s[i]] += 1
        
        ss = list(set(s))
        maxOdd = 0
        minEven = 101
        for i in range(len(ss)):
            if freqs[ss[i]] % 2 == 0:
                minEven = min(minEven, freqs[ss[i]])
            else:
                maxOdd = max(maxOdd, freqs[ss[i]])

        
        return maxOdd - minEven


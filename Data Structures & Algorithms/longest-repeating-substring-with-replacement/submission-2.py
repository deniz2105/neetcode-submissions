class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = {}
        maxFreq = 1
        maxLen = 1
        slowPointer = 0
        charDict[s[0]] = 1
        maxFreqChar = s[0]
        for i in range(1,len(s)):
            if s[i] not in charDict:
                charDict[s[i]] = 1
            else:
                charDict[s[i]] += 1
            
            if charDict[s[i]] > maxFreq:
                maxFreq = charDict[s[i]]
                maxFreqChar = s[i]
            
            while (i - slowPointer + 1) - maxFreq >k:
                charDict[s[slowPointer]] -=1
                if s[slowPointer] == maxFreqChar:
                    maxFreq -=1
                if charDict[s[slowPointer]] == 0:
                    charDict.pop(s[slowPointer], None)
                slowPointer +=1
                currMax = max(charDict.values())
                if maxFreq != currMax:
                    for key, v in charDict.items():
                        if v == currMax:
                           maxFreqChar = key
                           maxFreq = v
            maxLen = max(maxLen, i - slowPointer +1)
        return maxLen




        
            
            
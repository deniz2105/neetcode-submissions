class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def findMaxRecurrence(d):
            maxVal = -1
            maxChar = None
            for key, v in d.items():
                if v > maxVal:
                    maxChar= key
                    maxVal = v
            
            return maxChar

        charDict = defaultdict(int)

        maxCount = 1
        maxElement = s[0]
        charDict[s[0]]=1
        i = 0
        for j in range(1,len(s)):
            charDict[s[j]] +=1
            maxElement = findMaxRecurrence(charDict)
            maxVal = charDict[maxElement] + k
            while j - i+1> maxVal:
                charDict[s[i]] -= 1
                i +=1
                maxElement = findMaxRecurrence(charDict)
                maxVal = charDict[maxElement] + k

            
            maxCount = max(maxCount, j-i+1)
        
        return maxCount
            
            



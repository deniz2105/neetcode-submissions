class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        charDict = {}
        if len(s) < k:
            return 0

        for i in range(k):
            if s[i] not in charDict:
                charDict[s[i]] = 1
            else:
                charDict[s[i]] +=1
        count = 0
        if len(charDict) == k:
            count +=1

        j =0

        for i in range(k, len(s), 1):
            charDict[s[j]] -=1
            if charDict[s[j]] == 0:
                charDict.pop(s[j], None)
            j+=1
            if s[i] not in charDict:
                charDict[s[i]] = 1
            else:
                charDict[s[i]] +=1
            if len(charDict) == k:
                count +=1
            
        return count


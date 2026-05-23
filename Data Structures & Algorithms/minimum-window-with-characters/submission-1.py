class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def containsChars(sDict: [str, int], tDict: [str, int]) -> bool:
            for k, v in tDict.items():
                if k not in sDict or sDict[k] < v:
                    return False
            return True
        tDict = {}
        for i in range(len(t)):
            if t[i] not in tDict:
                tDict[t[i]] = 1
            else:
                tDict[t[i]] += 1
        
        windowDict = {}

        left = 0
        right = 0
        minWindow = s + "a"

        while right in range(0, len(s)):
            if s[right] not in windowDict:
                windowDict[s[right]] = 1
            else:
                windowDict[s[right]] += 1
            while right > left and ((s[left] not in tDict) or (windowDict[s[left]] > tDict[s[left]])):
                windowDict[s[left]] -=1
                left +=1
            if containsChars(windowDict, tDict):
                if len(s[left:right+1]) < len(minWindow):
                    minWindow = s[left:right+1]
            
            right+=1
        right -=1
        while right > left and ((s[right] not in tDict) or (windowDict[s[right]] > tDict[s[right]])):
                windowDict[s[right]] -=1
                right -=1
        
        if containsChars(windowDict, tDict):
             if len(s[left:right+1]) < len(minWindow):
                    minWindow = s[left:right+1]
        if len(minWindow) > len(s):
            return ""
        return minWindow
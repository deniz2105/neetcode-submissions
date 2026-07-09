class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charDict = {}
        for c in magazine:
            if c not in charDict:
                charDict[c] = 1
            else:
                charDict[c] += 1
        
        for c in ransomNote:
            if c not in charDict:
                return False
            if charDict[c] == 0:
                return False
            charDict[c] -=1
        
        return True
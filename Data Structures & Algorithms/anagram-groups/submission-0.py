class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sortString(w: str) -> str:
            charArr = []
            for c in w:
                charArr.append(c)
            charArr.sort()
            return ''.join(charArr)
        wordDict = {}
        for s in strs:
            sortedS = sortString(s)
            if sortedS not in wordDict:
                wordDict[sortedS] = []
            wordDict[sortedS].append(s)
        anagrams = []
        for _,value in wordDict.items():
            anagrams.append(value)
        return anagrams

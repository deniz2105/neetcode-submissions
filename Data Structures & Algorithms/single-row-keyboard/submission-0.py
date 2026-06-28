class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        kDict = {}
        for i in range(len(keyboard)):
            kDict[keyboard[i]] = i
        curr = 0
        time = 0
        for i in range(len(word)):
            time += abs(kDict[word[i]]-curr)
            curr = kDict[word[i]]
        return time
            
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newString = ""
        minLength = min(len(word1), len(word2))

        for i in range(0, minLength):
            newString += word1[i]
            newString += word2[i]
        
        if minLength == len(word1):
            for i in range(minLength, len(word2)):
                newString += word2[i]
        else:
            for i in range(minLength, len(word1)):
                newString += word1[i]
        return newString
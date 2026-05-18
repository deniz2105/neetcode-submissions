class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = 201
        for s in strs:
            curr = len(s)
            if curr<minLength:
                minLength = curr
        firstWord = strs[0]
        for i in range(minLength):
            for j in range(1, len(strs)):
                if strs[j][i] != firstWord[i]:
                    return firstWord[:i]
        return firstWord[:minLength]
            





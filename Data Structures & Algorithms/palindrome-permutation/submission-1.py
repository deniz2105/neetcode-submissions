class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        charCount = {}
        for i in range(len(s)):
            if s[i] not in charCount:
                charCount[s[i]] = 1
            else:
                charCount[s[i]] += 1
        oddFound = False
        ss = list(set(s))
        for i in range(len(ss)):
            if charCount[ss[i]] % 2 != 0:
                if oddFound:
                    return False
                oddFound = True
        return True
        
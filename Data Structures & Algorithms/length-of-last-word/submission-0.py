class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        idx = len(words) -1
        while idx >=0:
            if words[idx] != "":
                return(len(words[idx]))
            idx -=1
        return 0
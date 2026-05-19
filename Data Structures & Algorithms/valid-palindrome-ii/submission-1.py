class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s:str) -> bool:
            left = 0
            right = len(s)-1
            while left <= right:
                if s[left] != s[right]:
                    return False
                left +=1
                right -=1
            return True
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return isPalindrome(s[:left]+s[left+1:]) or isPalindrome(s[:right]+s[right+1:]) 
            left +=1
            right -=1
        return True
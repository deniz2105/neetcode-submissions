# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        curr = (1+n) //2
        pick = guess(curr)
        hi = n
        lo = 1
        while pick != 0:
            if pick == -1:
                hi = curr-1
            else:
                lo = curr +1
            curr = (lo+hi)//2
            pick = guess(curr)
        return curr
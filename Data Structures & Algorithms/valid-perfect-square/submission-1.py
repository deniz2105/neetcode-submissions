class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num 

        while left <= right:
            curr = (left + right)//2 #8 
            print(curr)

            currsq = curr * curr # 64

            if currsq == num:
                return True
            
            if currsq < num: # 64 < 16
                left = curr + 1
            else:
                right = curr-1 
        
        return False
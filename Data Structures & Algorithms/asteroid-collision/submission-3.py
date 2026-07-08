class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            if len(s) == 0:
                s.append(a)
                continue
            if (s[-1] >0 and a > 0) or (s[-1] < 0 and a < 0):
                s.append(a)
                continue
            while len(s)>0 and abs(s[-1]) < abs(a) and s[-1] > 0 and a < 0:
                s.pop()
            if len(s) == 0:
                s.append(a)
                continue
            
                
            if abs(s[-1]) > abs(a) and (s[-1] > 0 and a < 0):
                continue
            elif abs(s[-1]) == abs(a) and (s[-1] > 0 and a < 0):
                s.pop()
            else:
                s.append(a)
            
            
            
            
        return s

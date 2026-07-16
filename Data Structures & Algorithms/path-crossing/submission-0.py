class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinates = set()
        coordinates.add((0,0))
        curr = (0,0)
        for c in path:
            x = curr[0]
            y = curr[1]
            if c == 'N':
                y +=1
            elif c == 'S':
                y -=1
            elif c == 'E':
                x -=1
            elif c == 'W':
                x += 1
            curr = (x,y)
            if curr in coordinates:
                return True
            else:
                coordinates.add(curr)
        return False

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        resp = []

        visited = set()
        visited.add((0,0))
        resp.append(matrix[0][0])
        currR = 0
        currC = 0


        dirs = ((0,1),(1,0),(-1,0),(0,-1))

        maxlen = len(matrix[0]) * len(matrix)
        dirPointer = 0
        while len(resp) < maxlen:
            if (currR+dirs[dirPointer][0], currC+dirs[dirPointer][1]) in visited or currR+dirs[dirPointer][0] >= len(matrix) or currC+dirs[dirPointer][1] >= len(matrix[0]) or currC+dirs[dirPointer][1] < 0:
                if dirPointer +1 == len(dirs):
                    dirPointer = 0
                else:
                    dirPointer +=1
                continue
            currR = currR+dirs[dirPointer][0]
            currC = currC+dirs[dirPointer][1]
            resp.append(matrix[currR][currC])
            visited.add((currR, currC))
        return resp


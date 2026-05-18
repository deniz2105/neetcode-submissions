class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lenX = len(matrix)
        lenY = len(matrix[0])

        lo = 0
        hi = (lenX * lenY)-1

        while lo <= hi:
            curr = (lo + hi)//2
            x = int(curr/lenY)
            y = int(curr%lenY)
            if matrix[x][y] == target:
                return True
            
            elif target > matrix[x][y]:
                lo = curr +1
            elif target < matrix[x][y]:
                hi = curr -1
        return False
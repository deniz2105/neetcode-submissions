class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort()
        slowPointer = 0
        resp = []

        for i in range(len(arr)):
            if len(resp) < k:
                resp.append(arr[i])
            else:
                if abs(resp[0] - x) > abs(arr[i]-x):
                    resp.pop(0)
                    resp.append(arr[i])
        
        return resp


            



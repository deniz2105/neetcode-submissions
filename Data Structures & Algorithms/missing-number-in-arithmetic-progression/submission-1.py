class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        difference = abs((arr[len(arr) - 1] - arr[0]) // (len(arr)))

        hi = len(arr) - 1
        lo = 0
        curr = (lo + hi) // 2
        while lo < hi:
            if abs(arr[curr]-arr[curr+1]) != difference:
                break
            elif abs(arr[curr] - arr[lo]) > ((curr - lo) * difference):
                hi = curr - 1
            else:
                lo = curr + 1
            curr = (lo + hi) // 2

        if arr[len(arr) - 1] < arr[0]:
            difference = -difference
        return arr[curr] + difference

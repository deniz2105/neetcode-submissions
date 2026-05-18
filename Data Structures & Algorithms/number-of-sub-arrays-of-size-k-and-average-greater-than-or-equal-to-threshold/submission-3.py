class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = 0
        subarraysAT = 0
        for i in range(0, k):
            total+=arr[i]
        currAvg = total/k
        if currAvg >= threshold:
            subarraysAT += 1
        
        for i in range(k, len(arr)):
            total -= arr[i-k]
            total += arr[i]
            currAvg = total/k
            if currAvg >= threshold:
                subarraysAT += 1
        return subarraysAT



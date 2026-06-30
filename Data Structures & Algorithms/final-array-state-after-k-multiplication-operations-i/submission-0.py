class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        li = []
        for i in range(len(nums)):
            li.append([nums[i], i])
        
        heapq.heapify(li)
        for i in range(k):
            curr = heapq.heappop(li)
            curr[0] = curr[0] * multiplier
            heapq.heappush(li, curr)
        
        for i in li:
            nums[i[1]] = i[0]
        return nums

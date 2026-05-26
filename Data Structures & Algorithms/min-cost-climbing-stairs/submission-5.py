class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for i in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        print(dp)
        return min(dp[len(dp)-2], dp[len(dp)-1])


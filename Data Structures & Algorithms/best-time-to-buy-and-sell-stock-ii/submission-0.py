class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        costBasis = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > costBasis:
                profit += (prices[i]-costBasis)
            costBasis = prices[i]
        return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        MIN=prices[0]
        for i in range(len(prices)):
            MIN=min(MIN,prices[i])
            profit=max(prices[i]-MIN,profit)
        return profit
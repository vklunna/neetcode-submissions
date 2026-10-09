class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        best = 0
        for i in prices:
            best = max(best, i-cheapest)
            cheapest = min(cheapest, i)
        return best

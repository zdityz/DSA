class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        max_profit = 0
        for i in prices:
            if i<cheapest:
                cheapest = i
            profit = i-cheapest
            if profit > max_profit:
                max_profit = profit
        return max_profit

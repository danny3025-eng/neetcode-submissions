class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        next_buy = next_sell = 0
        cur_buy = cur_Sell = 0

        for i in range(n - 1, -1, -1):
            cur_buy = max(next_buy, -prices[i] + next_sell)
            cur_sell = max(next_sell, prices[i] + next_buy)
            next_buy = cur_buy
            next_sell = cur_sell

        return cur_buy

        
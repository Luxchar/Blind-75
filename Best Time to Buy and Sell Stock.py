# set min price var and max_price
# go through array and store min price if min_price < current
# for each day check if current - min_prices is > max_prices

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit

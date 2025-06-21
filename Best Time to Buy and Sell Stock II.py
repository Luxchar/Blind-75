# we need maximum amount of profits
# we can sell and buy on the same day

# loop through prices
# if the next day makes me a profit over today's price, add the amount of profits made

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                maxProfit += prices[i+1] - prices[i]

        return maxProfit
            
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            max_profit = max(sell-buy, max_profit)
            if buy > prices[left+1]:
                left += 1
            right += 1
        return max_profit

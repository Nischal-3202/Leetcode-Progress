class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cheapest_price=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if cheapest_price > prices[i]:
                cheapest_price=prices[i]
            profit=prices[i]-cheapest_price
            if profit > max_profit:
                max_profit=profit
        return max_profit

        
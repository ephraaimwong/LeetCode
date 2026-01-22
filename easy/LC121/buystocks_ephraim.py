class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        ---- Solution Intent ----
        Calculate current profit at current day. Update lowest price and maxprofit as we loop.
        """
        lowestPrice = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < lowestPrice: #update if new low is found
                lowestPrice = prices[i]
            currentProfit = prices[i] - lowestPrice #profit from current lowest to today
            if currentProfit > maxProfit: #update profit if new max found
                maxProfit = currentProfit
        return maxProfit #if no profit above 0 is found, maxProfit was init as 0 :)
class Solution(object):
    def maxProfit(self, prices):
     n=len(prices)
     min_price=prices[0]
     max_profit=0
     for i in range(n):
        if prices[i]<min_price:
            min_price=prices[i]
        else:
            current_price=prices[i]-min_price
            max_profit=max(current_price,max_profit)

     return max_profit


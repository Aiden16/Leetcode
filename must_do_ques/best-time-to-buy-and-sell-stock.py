class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('infinity')
        #max profit
        max_profit = 0
        
        for price in prices:
            min_price=min(price,min_price)
            profit=price-min_price
            max_profit = max(profit,max_profit)
        return max_profit
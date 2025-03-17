#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        buying_price = prices[0]

        for i in range(1, len(prices)):
            if buying_price > prices[i]:
                buying_price = prices[i]
            
            if profit < (prices[i] - buying_price):
                profit = prices[i] - buying_price
        return profit
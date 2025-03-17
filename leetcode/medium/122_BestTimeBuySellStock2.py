class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(day, holding):
            # Base case: last day no profit
            if day == len(prices):  
                return 0

            # see if already see this case from memo
            if (day, holding) in memo:
                return memo[(day, holding)]

            if holding == 0: # when not having stock
                # add to profit (negative because not having stock)
                # + dp(day + 1, 1) mean the previous case where WITH stock
                # dp(day + 1, 0) means WITHOUT stock
                total_profit = max(-prices[day] + dp(day + 1, 1), dp(day + 1, 0))
            else:  # when having stock
                total_profit = max(prices[day] + dp(day + 1, 0), dp(day + 1, 1))
            memo[(day, holding)] = total_profit
            return total_profit

        return dp(0, 0)  # starting from first day
class Solution(object):
    def maxProfit(self, prices, fee):
        hold = -prices[0]     # Max profit when holding a stock
        cash = 0              # Max profit when not holding

        for price in prices[1:]:
            cash = max(cash, hold + price - fee)   # Sell today
            hold = max(hold, cash - price)         # Buy today

        return cash

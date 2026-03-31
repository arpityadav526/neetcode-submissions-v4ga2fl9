class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min=prices[0]
        max_profit=0


        for price in prices :
            if price<min:
                min=price

            profit=price-min
            max_profit=max(max_profit, profit)
        return max_profit

            

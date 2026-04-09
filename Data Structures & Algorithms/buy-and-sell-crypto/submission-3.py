  

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0  # Buy pointer
        sell = 1  # Sell pointer
        max_profit = 0  # Initialize max profit

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                # Calculate the profit
                profit = prices[sell] - prices[buy]
                # Update the maximum profit found so far
                max_profit = max(max_profit, profit)
            else:
                # If current buy price is greater or equal to the sell price,
                # move the buy pointer to the sell position (because we should
                # consider the lowest possible price to buy)
                buy = sell
            # Always move the sell pointer forward
            sell += 1
        
        return max_profit             

                 



        
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum=prices[0]
        maximum_profit=0
        for min in range(len(prices)) :
            if prices[min] <minimum:
                minimum=prices[min]
            profit= prices[min]-minimum 
            if profit > maximum_profit:
                maximum_profit = profit

        return maximum_profit
                # min_index=min
        # max_price= prices[min_index]
        # maxi=min_index
        # for max in range (min_index +1 ,len(prices)):
        #     if prices[max]> max_price:
        #         max_price=prices[max]
        #         maxi=max
        
        # return prices[maxi] -  prices[min_index] 

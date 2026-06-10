
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices),1):
                price_range = prices[j] - prices[i]
                if price_range > 0 and price_range > res:
                    res = price_range
        return res



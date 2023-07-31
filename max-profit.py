class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = 0
        sellingPrice = 0
        gain = 0
        for i in range(len(prices)):
            if prices[buyingPrice] > prices[i]:
                buyingPrice = i
                sellingPrice = i
            if prices[sellingPrice] < prices[i]:
                sellingPrice = i
            gainApp = prices[sellingPrice] - prices[buyingPrice]
            if gainApp > gain:
                gain = gainApp
        return gain
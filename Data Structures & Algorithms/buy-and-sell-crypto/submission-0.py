class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0  #بیشترین سودی که تا الان دیده‌ایم.
        minBuy = prices[0]  #کمترین قیمتی که تا الان دیده‌ایم (بهترین زمان خرید).
        for sell in prices:
            maxP = max(maxP, sell-minBuy)
            minBuy = min(minBuy, sell)
        return maxP

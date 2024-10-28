"""
给定数组prices,prices[i]是第i天的价格;
只可以某一天买入,另一天卖出;
求最大利润;
prices = [7, 1, 5, 3, 6, 4] --> 第1天买,第4天卖 --> 6 - 1 = 5
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        # 假设当天卖出，算当前的最高利润
        for price in prices:
            # 先计算当前的最大利润，这样只是用当天之前的最小值来计算的
            # 比如[2, 3, 1, 4]在2的位置时，最小值是2，1 - 2 = -1，过了这一轮，最小值才是1
            maxprofit = max(price - minprice, maxprofit)
            # 更新最小值
            minprice = min(price, minprice)
        return maxprofit
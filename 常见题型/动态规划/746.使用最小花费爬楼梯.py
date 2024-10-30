"""
给出cost数组,cost[i]是楼梯第i个台阶往上爬需要支付的费用;
一旦支付这个费用,可以往上爬1个或2个台阶;
从下标为0或下标为1的位置开始爬楼梯;
计算最小花费;
[10,15,20] --> 从1开始,爬1层 --> 15
[1,100,1,1,1,100,1,1,100,1] --> 从0开始 --> 1 + 1 + 1 + 1 + 1 + 1 = 6
"""
# dp[i]
#   第i阶的最小花费
# 递推公式
#   dp[n] = min(dp[n - 2] + cost[n - 2], dp[n - 1] + cost[n - 1])
#   [n-2阶(A)]    [n-1阶(B)]    [n阶(C)]
#   两种情况取最小:
#           A爬2阶+A ----> min_cost(A) + cost(C)
#           B爬2阶+B ----> min_cost(B) + cost(B)
# 初始值
#   dp[0] = 0
#   dp[1] = 0
# 方向
#   从前向后
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        for i in range(2, len(cost) + 1):
            mincost = min(dp[0] + cost[i - 2], dp[1] + cost[i - 1])
            dp[0] = dp[1]
            dp[1] = mincost
        return dp[1]
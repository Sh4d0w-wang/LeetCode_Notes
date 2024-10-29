"""
F(n) = F(n - 1) + F(n - 2),F(0) = 0,F(1) = 1
n = 2 --> F(2) = F(1) + F(0) = 1 + 0 = 1
给n求数字
"""
# 动态规划四部曲
# 1.    确定dp[i]的含义 
#   第i个数字是dp[i]

# 2.    递推公式
#   dp[i] = dp[i - 1] + dp[i - 2]

# 3.    dp数组如何初始化
#   dp[0] = 0,dp[1] = 1

# 4.    遍历顺序
#   从前向后
class Solution:
    # 写法1
    def fib_1(self, n: int) -> int:
        # 0 1 2 3 4 5 6 7
        # 0 1 1 2 3 5 8
        dp = [0, 1]
        if n == 0:
            return dp[0]
        elif n == 1:
            return dp[1]
        else:
            for i in range(2, n+1):
                dp.append(dp[i - 1] + dp[i - 2])
            return dp[n]
    # 基于写法1优化（不存数组，每回合改变dp[0]和dp[1]）
    def fib_2(self, n: int) -> int:
        dp = [0, 1]
        if n == 0:
            return dp[0]
        elif n == 1:
            return dp[1]
        else:
            res = 0
            for i in range(2, n+1):
                res = dp[0] + dp[1]
                dp[0] = dp[1]
                dp[1] = res
            return res
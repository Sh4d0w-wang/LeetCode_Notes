"""
有n阶楼梯,每次可以爬1个或2个台阶,有多少种方法爬完;
n = 2 --> [1 + 1]和[2]---两种
n = 3 --> [1 + 1 + 1]和[1 + 2]和[2 + 1]---三种
"""
# dp[i]
#   i阶数有dp[i]种爬法
# 递推公式
#   dp[n] = dp[n - 1] + dp[n - 2]
# 初始值
#   dp[0] = 0, dp[1] = 1, dp[2] = 2, dp[3] = 3
# 方向
#   从前向后
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        if n < 3:
            return dp[n]
        else:
            for i in range(3, n + 1):
                num = dp[1] + dp[2]
                dp[1] = dp[2]
                dp[2] = num
            return dp[2]
"""
给一个正整数n,生成从1~n^2的所有元素;
且元素按照顺时针顺序螺旋排列在n*n的正方形矩阵中;
n = 3 --> 1 ~ 9
            1  2  3
            8  9  4
            7  6  5
--> [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
"""
class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        # 定义矩阵
        res = [[0 for _ in range(n)] for _ in range(n)]
        # 上下左右边界的起始位置
        left, right, top, bottom = 0, n - 1, 0, n - 1
        # 当前该填写的值
        num = 1
        while num <= n * n:
            # 若将坐标也放入for里面++到话，会错位（导致下一轮直接覆盖了上一轮写的），所以利用上下左右边界的值来定位
            # 从左边界到右边界
            for i in range(left, right + 1):
                res[top][i] = num
                num += 1
            top += 1
            # 从上边界到下边界
            for i in range(top, bottom + 1):
                res[i][right] = num
                num += 1
            right -= 1
            # 从右边界到左边界
            for i in range(right, left - 1, -1):
                res[bottom][i] = num
                num += 1
            bottom -= 1
            # 从下边界到上边界
            for i in range(bottom, top - 1, -1):
                res[i][left] = num
                num += 1
            left += 1
        return res

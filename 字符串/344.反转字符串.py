"""
将字符串s反转,不能申请空间,原地反转字符串;
s = ["h","e","l","l","o"] --> ["o","l","l","e","h"]
"""
class Solution:
    # 解法1
    # 双指针法
    def reverseString_1(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        # 相等时就不用交换了
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
    # 解法2
    # 切片赋值语法
    def reverseString(self, s: List[str]) -> None:
        # s[:] = s[::-1] 是切片赋值语法，表示用 s[::-1] 替换 s 中的元素。
        # 注意不能写成 s = s[::-1]，因为 s 只是形参，修改 s 不会影响函数外部传入的实参。
        # 注意这不是原地操作，需要 O(n) 额外空间。
        s[:] = s[::-1]
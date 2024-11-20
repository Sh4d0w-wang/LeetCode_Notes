"""
给一个字符串s和整数k
从头开始计算,计数至2k个字符,就反转这2k个字符中前k个字符
剩余字符小于k个,则剩余的全部反转
剩余字符小于2k,但大于或等于k个,则反转前k个字符
s = "abcdefg", k = 2 --> s = "bacdfeg"
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        for i in range(0, len(list_s), 2 * k):
            # 内置方法:reversed(),反转list、tuple等
            list_s[i : i + k] = reversed(list_s[i : i + k])
        return "".join(list_s)
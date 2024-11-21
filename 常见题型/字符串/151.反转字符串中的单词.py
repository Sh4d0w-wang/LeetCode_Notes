"""
151.反转字符串中的单词
给一个字符串s,反转s中单词的顺序;
单词:由非空格字符组成的,s中至少一个空格将单词分隔开;
s = "the sky is blue" --> "blue is sky the"
s可能会存在前导空格、尾随空格、或单词间多个空格,返回时应单词间只有一个空格
"""
class Solution:
    # 解法1
    # 利用栈
    def reverseWords_1(self, s: str) -> str:
        s = list(s)
        stack = []
        res = []
        flag = 0
        for i in range(len(s)):
            if s[i] == " " and flag == 0 and i != len(s) - 1:
                continue
            elif s[i] == " " and flag > 0:
                temp_s = "".join(s[i - flag:i])
                stack.append(temp_s)
                flag = 0
            elif i == len(s) - 1 and s[i] != " ":
                temp_s = "".join(s[i - flag:i + 1])
                stack.append(temp_s)
            else:
                flag += 1
        while stack != []:
            res.append(stack.pop())
        res = " ".join(res)
        return res
    
    # 解法2
    # 利用语言特性
    def reverseWords_2(self, s: str) -> str:
        # 不能s.split(" ")
        # 这样的话,"the   abc      " --> ['the', '', '', 'abc', '', '', '', '', '', '']
        # split(" ")保留连续的空格，每个空格都被视为一个分隔符
        # split()默认自动处理多个连续的空白字符(空格、制表符、换行符等)
        list_s = s.split()
        rev_s = reversed(list_s)
        res = " ".join(rev_s)
        return res
    
    # 解法3
    # 双指针,从后往前遍历
    def reverseWords_3(self, s: str) -> str:
        res = []
        left = right = len(s) - 1
        while left >= 0 and left <= right:
            # 去除尾部空格/找单词尾部
            while s[left] == " " and left >= 0 and left <= right:
                left -= 1
            right = left
            # 找单词开头
            while s[left] != " " and left >= 0 and left <= right:
                left -= 1
            # 排除掉前导空格
            if left != right:
                res.append(s[left + 1:right + 1])
        res = " ".join(res)
        return res
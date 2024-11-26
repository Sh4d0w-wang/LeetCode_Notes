"""
s全部由小写字母组成,删除两个相邻且相同的字母;
s = "abbaca" --> "aaca" --> "ca"
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        index = 0
        while index < len(s):
            # 第一种情况:栈为空
            # 第二种情况:栈顶元素和当前字符不同
            if stack == [] or s[index] != stack[-1]:
                stack.append(s[index])
                index += 1
            # 当前字符与栈顶元素相同,两个都删除
            else:
                stack.pop()
                index += 1
        return "".join(stack)
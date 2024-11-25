"""
20.有效的括号
给定一个只包括"(", ")", "{", "}", "[", "]"的字符串s,判断字符串是否有效;
左右括号类型、顺序、数量必须相同;
s = "()" --> True
s = "(){}[]" --> True
s = "([)" --> False
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")":
                if not stack:
                    return False
                elif stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif i == "]":
                if not stack:
                    return False
                elif stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif i == "}":
                if not stack:
                    return False
                elif stack[-1] != "{":
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        else:
            return True
    # 优化版本
    def isValid_2(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack
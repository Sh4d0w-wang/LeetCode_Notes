"""
s = "aabaabaaf"
t = "aabaaf"
s中是否有t这个模式串
"""
# 易想思路
# s一个指针，从头遍历到尾
# t一个指针，从头遍历到尾
# 一个一个对比，直到t顶指针走完
def Sol_1( s : str, t : str ) -> bool:
    for i in range(len(s)):
        for j in range(len(t)):
            if i + j >= len(s):
                return False
            if s[i + j] != t[j]:
                break
        if s[i + j] == t[j] and j == len(t) - 1:
            return True
    return False

# KMP
# 求模式串到前缀表:[0, 1, 0, 1, 2, 0]（也就是next数组）
# 比如2是怎么得到的:aabaa
#   前缀:a, aa, aab
#   后缀:a, aa, baa
#   最长相等前后缀的长度为'aa','aa' = 2
# 这个2的意思是，前面有了一个相等的前缀，下次匹配直接从2下标开始
def KMP( s : str, t : str ) -> bool:
    # 初始化next数组
    next = [0] * len(t)
    # 前后缀的长度
    t_length = 0
    # 比较的话，是从1这个位置开始的（后缀的下标只可能在0之后）
    i = 1
    while i < len(t):
        if t[i] == t[t_length]:
            t_length += 1
            next[i] = t_length
            i += 1
        else:
            if t_length != 0:
                t_length = next[t_length - 1]
            else:
                next[i] = 0
                i += 1

    i = j = 0
    while i < len(s):
        if t[j] == s[i]:
            i += 1
            j += 1
        if j == len(t):
            print(i - j)
            return True
            j = next[j - 1]
        elif i < len(s) and t[j] != s[i]:
            if j != 0:
                j = next[j - 1]
            else:
                i += 1
    return False
"""
每个人i,均有一个胃口值g[i](必须要达到);
每个饼干j, 均有一个尺寸s[j];
s[j] > g[i]才能满足这个人,满足尽可能多的人;

g = [1, 2, 3]
s = [1, 1]
----> 1

g = [1, 2]
s = [1, 2, 3]
----> 2
"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 从小到大排序
        g.sort()
        s.sort()
        i = j = num = 0
        while i < len(s) and j < len(g):
            # 以饼干作参照,只要它小于最小的人胃口,直接舍弃
            if s[i] < g[j]:
                i += 1
            # 只要大于等于,则符合
            else:
                num += 1
                i += 1
                j += 1
        return num

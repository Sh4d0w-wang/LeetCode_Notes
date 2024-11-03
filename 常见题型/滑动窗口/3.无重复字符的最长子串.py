"""
给定字符串s,找出其中无重复字符的最长子串,返回其长度;
s = "abcabcbb" --> "abc" --> 3
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        maxlen, r = 0, -1
        for i in range(n):
            if i != 0:
                # 左指针向右移动一个,移除一个字符
                occ.remove(s[i - 1])
            # 移动右指针
            # 不在集合中就往里添
            # 在集合中就停止遍历,并在上面移去该值（r[该轮的] + 1 = i[下一轮的] - 1）
            while r + 1 < n and s[r + 1] not in occ:
                occ.add(s[r + 1])
                r += 1
            maxlen = max(maxlen, r - i + 1)
        return maxlen
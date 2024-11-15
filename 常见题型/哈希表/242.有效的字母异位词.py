"""
给s和t,确定t是否是s的异位词(s重新排列字母得到新的字符串t,且必须用到所有元素)
s = "abcd", t = "bdca" --> True
s = "abc", t = "cbq" --> False
s = "abc", t = "cb" --> False
"""
# 三种哈希表法
class Solution:
    # 解法1
    # 自己用数组搞一个26字母的哈希表，有一个则在其index位置处+1
    def isAnagram_1(self, s: str, t: str) -> bool:
        hashtable = [0] * 26
        for i in s:
            index = ord(i) - 97
            hashtable[index] += 1
        for i in t:
            index = ord(i) - 97
            if hashtable[index] != 0:
                hashtable[index] -= 1
            else:
                return False
        for i in hashtable:
            if i != 0:
                return False
        return True
    
    # 解法2
    # 利用字典作哈希表，使用了defaultdict的方法，同样是计数的原理
    def isAnagram_2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # 当key不在字典中时，默认将其的val设置为(int)-->0
        hashtable = collections.defaultdict(int)
        for c in s:
            hashtable[c] += 1
        for c in t:
            hashtable[c] -= 1
        for val in hashtable.values():
            if val != 0:
                return False
        return True
    
    # 解法3
    # 利用Counter方法直接统计
    def isAnagram_3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Counter是一个容器对象,主要的作用是用来统计散列对象（和字典差不多）
        hashtable = collections.Counter(s)
        for c in t:
            if hashtable[c] <= 0:
                return False
            hashtable[c] -= 1
        return True
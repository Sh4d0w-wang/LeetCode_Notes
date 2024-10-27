"""
给一个nums数组,返回里面的多数元素,出现次数大于(n/2)取下界
[2, 3, 2] --> 2
[2, 3, 3, 2] --> 2, 3
"""
class Solution:
    # 解法1
    # 哈希映射
    def majorityElement_1(self, nums: List[int]) -> int:
        # Counter 类会统计 nums 列表中每个元素出现的次数
        # counts = 数字:次数
        counts = collections.Counter(nums)
        # 告诉max函数：
        # 以count.get函数获取每个键的计数值，并根据这个计数值来确定哪个键是最大的
        # 一堆元素，通过"key"参数获取这堆元素的另外特征，找这些特征中最大的，并返回这个元素本身
        return max(counts.keys(), key = counts.get)
    # 解法2
    # 由于多数大于n/2，所以排完序后，取n//2的元素即可
    # 1 1 1 2 2 2 2 --> 7//2 = 3 --> 2
    # 1 1 1 2 --> 4//2 = 2 --> 1
    def majorityElement_2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
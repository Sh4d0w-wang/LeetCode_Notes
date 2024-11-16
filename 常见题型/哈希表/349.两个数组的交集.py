"""
两个数组nums1和nums2,返回它们的交集,元素的顺序不考虑
nums1 = [1, 2, 3], nums2 = [2, 4, 5, 3] --> [2, 3]或[3, 2]
"""
class Solution:
    # 直接利用set集合
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hash_set = set(nums1)
        nums2_hash_set = set(nums2)
        res = []
        for i in nums2_hash_set:
            if i in nums1_hash_set:
                res.append(i)
        return res
    # 另一种写法
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # python集合可以直接实现交集的运算
        return list(set(nums1) & set(nums2))

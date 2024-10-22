"""
nums1 = [1, 2, 2, 4, 0, 0, 0]
nums2 = [3, 5, 7]
--> nums1 = [1, 2, 2, 3, 4, 5, 7],递增,不能生成新的list给nums1
"""
class Solution:
    # 解法1
    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 从后往前依次遍历，大的从后往前填
        i = m - 1
        j = n - 1
        k = m + n - 1
        while (j >= 0):
            if (i < 0 or nums2[j] > nums1[i]):
                nums1[k] = nums2[j]
                k = k - 1
                j = j - 1
            else:
                nums1[k] = nums1[i]
                k = k - 1
                i = i - 1
    # 解法2
    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 将nums2放到nums1的后面，然后直接对nums1进行排序
        nums1[m:] = nums2
        nums1.sort()
    # 解法3
    def merge_3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 双指针，不好
        # 借助一个新的list存放
        new_list = []
        p1, p2= 0, 0
        # 当两指针其中任意一个小于各自list的长度时都执行
        while (p1 < m and p2 < n):
            # 得首先判断其中任意一个有没有遍历完成
            if p1 == m:
                new_list.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                new_list.append(nums1[p1])
                p1 += 1
            # 接下来才是遍历过程中，谁大放谁
            elif nums1[p1] <= nums2[p2]:
                new_list.append(nums1[p1])
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                new_list.append(nums2(p2))
                p2 += 1
        # 这边不能用nums1 = new_list，因为这个语句创建了一个新的对象
        # 下面这个语句才是赋值
        nums1[:] = new_list
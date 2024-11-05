"""
给定nums,删除nums中值为val的元素,更改原nums,并返回不相同元素的个数
[3, 2, 3, 3], val = 3 --> 1 --> [2, 2]
"""
class Solution:
    # 双指针
    def removeElement(self, nums: List[int], val: int) -> int:
        # i代表下一个不同元素所要放的下标
        # j一直向后遍历
        i, j = 0, 0
        while j < len(nums):
            # 不同则将该元素放到i的位置
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            # 相同则继续往后遍历
            else:
                j += 1
        return i
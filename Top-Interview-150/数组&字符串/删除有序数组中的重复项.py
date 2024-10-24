"""
非严格递增nums,删除重复元素,返回删除后的新长度,元素的相对顺序保持一致;
nums = [1, 1, 2] --> 2, nums = [1, 2, _]
nums = [0, 0 ,1, 1, 2, 3, 3, 4] --> 5, nums = [0, 1, 2, 3, 4]
"""
class Solution:
    # 解法1
    # 双指针法，一个始终指向最终确定list的最后一个，另一个一直往后遍历
    # 与最后一个相同则继续往后，不同则将其赋值到list到后一个来
    # 但若是list中的数字随意排序，就不能这么搞，得先排个序
    def removeDuplicates_1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        else:
            i, j = 0, 1
            while i < len(nums) and j < len(nums):
                # 不同则向后增加一个并赋值
                if nums[i] != nums[j]:
                    i += 1
                    nums[i] = nums[j]
                    j += 1
                # 相同就往后
                else:
                    j += 1
            return i + 1
"""
给一个有序数组nums,删除重复元素,使得出现次数超过2次的只出现2次;
返回新长度,不要申请新空间;
nums = [1, 1, 1, 2, 2, 4] --> nums = [1, 1, 2, 2, 4]
"""
class Solution:
    # 解法1
    # 同前面一个的双指针法，增加了一个计数器
    def removeDuplicates_1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        else:
            i, j, count= 0, 1, 1
            while i < len(nums) and j < len(nums):
                if nums[i] != nums[j]:
                    i += 1
                    nums[i] = nums[j]
                    j += 1
                    count = 1
                # count为1的原因是：已经有一个nums[i]在最后面了，剩余还要一个就行
                elif count > 0 and nums[i] == nums[j]:
                    i += 1
                    nums[i] = nums[j]
                    j += 1
                    count -= 1
                # 两次以上的
                else:
                    j += 1
            return i + 1
    # 解法2
    # 不带计数器，用一个flag来代替（拓展思路）
    def removeDuplicates_2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        else:
            i, j= 0, 1
            flag = False
            while i < len(nums) and j < len(nums):
                if nums[i] != nums[j]:
                    i += 1
                    nums[i] = nums[j]
                    j += 1
                    flag = False
                elif nums[i] == nums[j] and flag == False:
                    i += 1
                    nums[i] = nums[j]
                    j += 1
                    flag = True
                # 两次以上的
                else:
                    j += 1
            return i + 1
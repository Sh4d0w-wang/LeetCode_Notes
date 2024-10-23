"""
给出nums数组和一个值val,移除nums中所有val,返回剩余元素数量k;
nums = [2, 3, 3, 2], val = 3; --> nums = [2, 2, _, _], k = 2
"""
class Solution:
    # 解法1
    # 双指针
    # left一直往后遍历，直到遇到为val的
    # right一直往前遍历，赋值给nums[left]->(直到遇到一个不为val的，left才继续向后)
    def removeElement_1(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1
        return left
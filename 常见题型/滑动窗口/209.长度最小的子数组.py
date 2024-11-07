"""
给正整数数组nums和一个target,
找出数组中满足其和>=target的最小长度的子数组,返回长度,没有则返回0;

nums = [2, 3, 1, 2, 4, 3], target = 7 --> [4, 3],2
"""
class Solution:
    # 滑动窗口
    # 大体思路:
    # 以右边来循环，大于target则不停的删去最左边的值，直到找到最小长度
    # 小于target则右边加一个
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = num_sum = 0
        minlen = len(nums) + 1
        while right < len(nums):
            num_sum += nums[right]
            # 当和大于等于target时
            while num_sum >= target:
                # 先计算长度
                minlen = min(minlen, right - left + 1)
                # 减去最左边的
                num_sum -= nums[left]
                left += 1
            right += 1
        return minlen % (len(nums) + 1)
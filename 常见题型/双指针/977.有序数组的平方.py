"""
给一个非递减的数组nums,返回每个数字的平方,组成一个新的数组,也是按照非递减顺序;
nums = [-7, -1, 0, 2, 3] --> [0, 1, 4, 9, 49]
"""
class Solution:
    # 解法1
    # 先平方，后直接排序
    def sortedSquares_1(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        return nums.sort()
    # 解法2
    # 双指针法
    # 因为最大的只可能出现在两端，从两边向中间遍历，最后逆一下即可
    def sortedSquares_2(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        res = []
        while left <= right:
            if nums[left]**2 < nums[right]**2:
                res.append(nums[right]**2)
                right -= 1
            else:
                res.append(nums[left]**2)
                left += 1
        return res[::-1]
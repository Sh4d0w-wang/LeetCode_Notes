"""
给定nums,和k,将nums向右轮转k个(右循环k个)
nums = [1, 2, 3, 4, 5], k = 2 --> [4, 5, 1, 2, 3]
"""
class Solution:
    # 超出时间限制
    def rotate_1(self, nums: List[int], k: int) -> None:
        while k > 0:
            # 最后一个赋值给temp
            temp = nums[len(nums) - 1]
            # 将0～倒数第二个赋值给1～最后
            nums[1:] = nums[:len(nums) - 1]
            nums[0] = temp
            k -= 1
    # 解法2
    # 第i个元素在（i + k）mod n的位置
    def rotate_2(self, nums: List[int], k: int) -> None:
        length = len(nums)
        new_Nums = [None] * length
        # [0, 1, 2, 3, 4, 5, 6], k = 2
        # nums[4] --> nums[6] --> (4 + 2) mod 7 = 6
        # nums[5] --> nums[0] --> (5 + 2) mod 7 = 0 
        # [0, 1], k = 3
        # nums[0] --> nums[1] --> (0 + 3) mod 2 = 1
        for i in range(length):
            new_Nums[(i + k) % length] = nums[i]
        nums[:] = new_Nums
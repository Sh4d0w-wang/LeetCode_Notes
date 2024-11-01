"""
给整数数组nums,和一个target目标,使nums中两数相加为target,返回下标;
一个元素只能使用一次,切答案唯一;
nums = [2, 7, 11, 15],target = 9 --> 2 + 7 = 9 --> 0, 1
"""
class Solution:
    # 解法1
    # 双指针,但速度很慢
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            # 第二个指针从i后面一个开始遍历
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                else:
                    j += 1
            i += 1
    # 解法2
    # 哈希表,map
    # 遍历到一个新元素时，检查是否有之前遍历过的目标数(target - nums[i])
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        # 遍历下标和元素
        for i, num in enumerate(nums):
            # 检索目标值是否遍历过
            if target - num in hashtable:
                return [hashtable[target - num], i]
            # 存入哈希表
            hashtable[nums[i]] = i
        return []
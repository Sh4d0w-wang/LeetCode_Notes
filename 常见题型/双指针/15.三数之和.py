"""
给一个nums,判断是否存在坐标不同的三个数相加为0,返回所有不重复的结果;

nums = [-1,0,1,2,-1,-4] --> [[-1,-1,2],[-1,0,1]]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # nums[first] > 0 时，直接跳出
        # first > 0 且nums[first] = nums[first - 1]时，跳过该元素，因为该元素所有可能的结果都取过了
        # second 和 third 在 (first,len(nums))两端
        #   当sum > 0时，third - 1，并跳过所有重复的nums[third]
        #   当sum < 0时，second + 1，并跳过所有重复的nums[second]
        #   当sum = 0时，记录到res中，两端同时往里跳过重复的值，以免后面取到相同结果
        first = 0
        while first < len(nums) - 2:
            if nums[first] > 0:
                break
            if first > 0 and nums[first] == nums[first - 1]:
                first += 1
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                sum = nums[first] + nums[second] + nums[third]
                if sum == 0:
                    while second < third and nums[second] == nums[second + 1]:
                        second += 1
                    while second < third and nums[third] == nums[third - 1]:
                        third -= 1
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1
                elif sum > 0:
                    while second < third and nums[third] == nums[third - 1]:
                        third -= 1
                    third -= 1
                else:
                    while second < third and nums[second] == nums[second + 1]:
                        second += 1
                    second += 1
            first += 1
        return res
"""
给一个nums和一个target,使有四个不同位置的数相加和为target;
nums = [1,0,-1,0,-2,2], target = 0 --> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""
class Solution:
    # 继续三数之和的方法
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # 先排序
        nums.sort()
        # first范围 (0, len(nums) - 3)
        # second范围 (1, len(nums) - 2)
        first = 0
        while first < len(nums) - 3:
            second = first + 1
            while second < len(nums) - 2:
                # 此处就不用判断前两个相加是否大于还是小于target了
                # 反例:[-5, -4, -3, -2, 1],target = -11 --> [-5, -4, -2, 1]
                # if nums[first] + nums[second] > target:
                #     break
                # third 和 fourth 范围 (second , len(nums) - 1)
                third = second + 1
                fourth = len(nums) - 1
                while third < fourth:
                        # 当四个相加 = target,直接append,跳过重复值,取到下一个元素
                        # 当四个相加 < target,跳过重复值,third + 1
                        # 当四个相加 > target,跳过重复值,fourth - 1
                    sum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if sum == target:
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
                        while third < fourth and nums[third] == nums[third + 1]:
                            third += 1
                        while third < fourth and nums[fourth] == nums[fourth - 1]:
                            fourth -= 1
                        third += 1
                        fourth -= 1
                    elif sum < target:
                        while third < fourth and nums[third] == nums[third + 1]:
                            third += 1
                        third += 1
                    else:
                        while third < fourth and nums[fourth] == nums[fourth - 1]:
                            fourth -= 1
                        fourth -= 1
                # 当nums[second] = nums[second - 1]时，下一个数，因为此值作为second的所有结果已经遍历过了
                while nums[second] == nums[second + 1] and second < len(nums) - 2:
                    second += 1
                second += 1
            # 当nums[first] = nums[first - 1]时，下一个数，因为此值作为first的所有结果已经遍历过了
            while nums[first] == nums[first + 1] and first < len(nums) - 3:
                first += 1
            first += 1
        return res
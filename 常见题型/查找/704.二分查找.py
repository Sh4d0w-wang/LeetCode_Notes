"""
搜索n个升序的nums中的target,返回下标,没有则返回-1;
[-1, 0, 3, 5, 9, 12], target = 9 --> 4
"""
class Solution:
    # 左闭右闭--[left, right]
    def search_1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # [1, 1]的情况符合,所以有等于号
        while left <= right:
            mid = (right + left) // 2
            # [left, mid]
            # nums[mid]已经大于target了，由于是闭区间，这个值不需要再比对，所以mid-1
            if nums[mid] > target:
                right = mid - 1
            # [mid, right]
            # nums[mid]已经小于target了，这个值不需要再比对，所以mid+1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
    # 左闭右开--[left, right)
    def search_2(self, nums: List[int], target: int) -> int:
        # 因为不包含右边界，right要加个1
        left, right = 0, len(nums)
        # [1, 1)的情况不符合,所以没有等于号
        while left < right:
            mid = (right + left) // 2
            # [left, mid)
            # nums[mid]已经大于target了，由于是开区间，这个值本来就不在范围内，不用+-
            if nums[mid] > target:
                right = mid
            # [mid, right)
            # nums[mid]已经小于target了，由于是闭区间，这个值不用再比对了，所以mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


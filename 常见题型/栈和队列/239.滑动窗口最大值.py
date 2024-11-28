"""
给一个数组nums,有一个大小为k的滑动窗口从最左侧移动到最右侧,
只能看到在窗口内的k个数字,每次仅向右移动一位,求窗口中的最大值;
nums = [1,3,-1,-3,5,3,6,7], k = 3 --> [3,3,5,5,6,7]
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
import collections
class Solution:
    # 超时
    # 使用单调队列,比较在队列中的最大值,时间复杂度:O(nk)
    def maxSlidingWindow_1(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque()
        res = []
        for i in range(k - 1):
            queue.append(nums[i])
        i = k - 1
        while i < len(nums):
            if len(queue) < k:
                queue.append(nums[i])
            if len(queue) == k:
                res.append(max(queue))
            queue.popleft()
            i += 1
        return res
    # 还是使用单调队列
    # 至少保留最大元素和第二大元素在队列中
    def maxSlidingWindow_2(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        # 使用zip(range(), range())可实现左右边界同时遍历
        # 左边界:i --> [1 - k, n - k],遍历窗口
        # 右边界:j --> [0, n - 1],遍历nums
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 若i > 0且队首元素是被删除的元素nums[i - 1],队首元素出队
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 删除deque内所有小于nums[j]的元素,以保持递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            # 将nums[j]添加至deque尾部
            deque.append(nums[j])
            if i >= 0:
                # 若已形成窗口，也就是i >= 0了,将队首元素(也就是最大值)添加到res
                res.append(deque[0])
        return res
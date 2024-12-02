"""
给一个数组nums和整数k,返回数组中第k个最大元素;
不是第k个不同元素,而是排序后的第k个元素
[3, 2, 1, 5, 6, 4], k = 2 --> 5
[3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4 --> 4
"""
import heapq
# heapq只能构造小根堆，要构造大根堆的话，可以让元素均为负，越大的在越下面
def findKthLargest(nums: list[int], k: int) -> int:
    minHeap = []
    for num in nums:
        if len(minHeap) < k:
            heapq.heappush(minHeap, num)
        elif num >= minHeap[0]:
            heapq.heappushpop(minHeap, num)
    return minHeap[0]
"""
给四个数组num1, nums2, nums3, nums4,每个长度为n;
计算有多少个(i, j, k, l)满足：
1. 0 <= i, j, k, l < n
2. nums1[i] + nums2[j] + nums[k] + nums[l] == 0

nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2] --> 1 + -2 + -1 + 2 = 0|2 + -1 + -1 + 0 = 0 --> 2
"""
class Solution:
    # 两组两组来遍历，这样复杂度就降到了n^2
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        hashtable = dict()
        # 将num1和nums2中的元素相加，存在哈希表中，并将次数记录下来
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] + nums2[j] in hashtable:
                    hashtable[nums1[i] + nums2[j]] += 1
                else:
                    hashtable[nums1[i] + nums2[j]] = 1
        # 接着遍历nums3和nums4，若0-nums3[k]-nums4[l]在哈希表中，将res与hashtable[val]相加
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                if 0 - nums3[k] - nums4[l] in hashtable:
                    res += hashtable[0 - nums3[k] - nums4[l]]
        return res
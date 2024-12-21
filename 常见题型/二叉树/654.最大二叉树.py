"""
给定一个不重复的数组nums,最大二叉树可以用下面的算法从nums递归构建:
1.创建一个根节点,其值为nums中最大值
2.递归地在最大值左边的子数组前缀上构建左子树
3.递归地在最大值右边的子数组前缀上构建右子树
返回nums构建的最大二叉树
nums = [3, 2, 1, 6, 0, 5] --> [6, 3, 5, null, 2, 0, null, null, 1]
最大值为6,左边是[3, 2, 1],右边是[0, 5]...
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
            if left > right:
                return None
            max_num = max(nums[left:right+1])
            max_num_index = nodes_hashtable[max_num]
            root = TreeNode(val = max_num)
            root.left = construct(left, max_num_index - 1)
            root.right = construct(max_num_index + 1, right)
            return root
        nodes_hashtable = dict()
        for i, val in enumerate(nums):
            nodes_hashtable[val] = i
        root = construct(0, len(nums) - 1)
        return root
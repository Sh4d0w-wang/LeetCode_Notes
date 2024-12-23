"""
给一个二叉搜索树的根节点root,返回树中任意两不同节点值之间的最小差值;
差值为正数;
root = [4,2,6,1,3] --> 1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 中序遍历,然后相邻两个相减,找最小
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)
        if not root:
            return 0
        inorder_list = []
        inorder(root)
        min_num = 1e9
        for i in range(0, len(inorder_list) -1):
            temp = abs(inorder_list[i + 1] - inorder_list[i])
            if temp <= min_num:
                min_num = temp
        return min_num
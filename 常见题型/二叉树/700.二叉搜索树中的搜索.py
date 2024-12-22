"""
给一个二叉搜索树(BST)的根节点root,和一个整数值val;
需要在BST中找到节点值为val的节点,并返回以该节点为根的树,否则返回null;
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root):
            if not root or root.val == val:
                return root
            if root.val < val:
                return dfs(root.right)
            if root.val > val:
                return dfs(root.left)
        return dfs(root)
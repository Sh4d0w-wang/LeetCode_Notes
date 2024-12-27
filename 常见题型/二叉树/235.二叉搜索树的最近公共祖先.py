"""
给定一个二叉搜索树,找到该树中两个指定节点的最近公共祖先;
root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8 --> 6
root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4 --> 2
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 解法1
    # 沿用二叉树的最近公共祖先,深度优先搜索
    def lowestCommonAncestor_1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root
    # 解法2
    # 利用二叉搜索树的特性
    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p,q均在左子树
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # p,q均在右子树
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
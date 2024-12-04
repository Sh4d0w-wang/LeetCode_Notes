"""
给一个二叉树的根节点root,返回此二叉树的前序遍历
root = [1, null, 2, 3] --> [1, 2, 3]
root = [1, 2, 3, 4, 5, null, 8, null, null, 6, 7, 9] --> [1, 2, 4, 5, 6, 7, 3, 8, 9]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        stack = []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res
"""
给一个二叉树的根节点root,返回此二叉树的中序遍历
root = [1, null, 2, 3] --> [1, 3, 2]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root:TreeNode):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        res = list()
        inorder(root)
        return res
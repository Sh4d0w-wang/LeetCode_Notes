"""
给一个二叉树的根节点,检查其是否对称;
root = [1,2,2,3,4,4,3] --> true
root = [1,2,2,null,3,null,3] --> false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 不停的往下递归，判断L.left和R.right、L.right和R.left是否相同
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(L, R):
            # L和R均为空
            if not L and not R:
                return True
            # L或R有一个为空，或者L的值与R的值不相同
            if not L or not R or L.val != R.val:
                return False
            # 继续判断L.left和R.right、L.right和R.left是否相同
            return recur(L.left, R.right) and recur(L.right, R.left)
        return not root or recur(root.left, root.right)
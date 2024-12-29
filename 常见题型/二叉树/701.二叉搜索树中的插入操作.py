"""
给定二叉搜索树的根节点root和要插入树中的值value,将值插入二叉搜索树;
返回插入后二叉搜索树的根节点;
新值和原始二叉搜索树中的任意节点值都不同;
注意,可能存在多种有效的插入方式,只要树在插入后仍保持为二叉搜索树即可;
root = [4,2,7,1,3], val = 5 --> [4,2,7,1,3,5]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 模拟
    # 遇到比当前节点小的往左，大的往右
    def insertIntoBST_1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node = root
        while node:
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            elif val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
        return root
    # 递归版本
    def insertIntoBST_2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(root, val):
            if not root:
                return TreeNode(val)
            if val < root.val:
                root.left = dfs(root.left, val)
            else:
                root.right = dfs(root.right, val)
            return root
        return dfs(root, val)
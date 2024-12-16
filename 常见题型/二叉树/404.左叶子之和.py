"""
给定一个二叉树root,返回其所有左叶子之和;
root = [3,9,20,null,null,15,7] --> 9 + 15 = 24
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 深度搜索
    # 写法1
    def sumOfLeftLeaves_1(self, root: Optional[TreeNode]) -> int:
        def dfs(root, pre, res):
            if not root:
                return
            # 当为叶节点且当前节点是上一个节点的左孩子
            if not root.left and not root.right and root == pre.left:
                res.append(root.val)
            dfs(root.left, root, res)
            dfs(root.right, root, res)
            return res
        res = dfs(root, root, [])
        sum = 0
        for i in res:
            sum += i
        return sum
    # 写法2
    def sumOfLeftLeaves_2(self, root: Optional[TreeNode]) -> int:
        def dfs(root, pre):
            if not root:
                return
            # 当为叶节点且当前节点是上一个节点的左孩子
            if not root.left and not root.right and root == pre.left:
                self.res += root.val
            dfs(root.left, root)
            dfs(root.right, root)
        self.res = 0
        dfs(root, root)
        return self.res
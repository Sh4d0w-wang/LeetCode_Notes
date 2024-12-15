"""
给一个二叉树,返回其从root到各个叶节点的路径;
root = [1,2,3,null,5] --> ["1->2->5","1->3"]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 使用深度优先遍历
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def getPath(root, path, res):
            if not root:
                return
            # 将当前节点值加入当前路径
            path += str(root.val)
            # 已经是叶子节点了,将path加入res
            if root.left == None and root.right == None:
                res.append(path)
            else:
                # 加上符号
                path += '->'
                # 遍历左
                getPath(root.left, path, res)
                # 遍历右
                getPath(root.right, path, res)
        res = []
        getPath(root, '', res)
        return res
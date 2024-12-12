"""
给定一个二叉树,判断是否是平衡二叉树
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 解法1
    # 从下往上,判断每个node的左右子树高度差是否小于等于1
    def isBalanced_1(self, root: Optional[TreeNode]) -> bool:
        # 返回当前顶点的高度
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            return max(left, right) + 1
        if not root:
            return True
        # 1.判断左右子树的高度差
        # 2.判断左孩子的左右子树高度差
        # 3.判断右孩子的左右子树高度差
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    # 解法2
    # 从下往上,判断每个节点的左右子树高度差,只要不符合,直接退出
    def isBalanced_2(self, root: Optional[TreeNode]) -> bool:
        def recur(root):
            # 当前为页节点
            if not root:
                return 0
            # 遍历左
            left = recur(root.left)
            # 之前的遍历已有不是平衡的
            if left == -1:
                return -1
            # 遍历右
            right = recur(root.right)
            # 之前的遍历已有不是平衡的
            if right == -1:
                return -1
            # 判断当前的左右高度是否小于等于1
            if abs(left - right) <= 1:
                # 返回高度(只要不是-1即可)
                return max(left, right) + 1
            else:
                return -1
        # 判断返回的值是否为-1
        return recur(root) != -1
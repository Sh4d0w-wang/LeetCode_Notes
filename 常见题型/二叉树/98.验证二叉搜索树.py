"""
给一个二叉树的根节点root,判断其是否是一个有效的二叉搜索树;
root = [2,1,3] --> True
root = [5,1,4,null,null,3,6] --> False
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 解法1
    # 中序遍历,之后应该是一个递增序列,不是则False
    def isValidBST_1(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)
        if not root:
            return True
        inorder_list = []
        inorder(root)
        val = inorder_list.pop()
        while inorder_list:
            temp_val = inorder_list.pop()
            if temp_val >= val:
                return False
            val = temp_val
        return True
    # 解法2
    # 从下往上,同时存储一个最大最小值的范围,不在这个范围之间则返回False
    def isValidBST_2(self, root: Optional[TreeNode]) -> bool:
        # float('-inf')代表负无穷大,反之无穷大
        # float('-inf')与任何负数相比均返回False
        # float('inf')与任何正数相比均返回False
        # 1e9和-1e9是具体的数值,有界限的
        def dfs(root, min_num = float('-inf'), max_num = float('inf')):
            if not root:
                return True
            if min_num >= root.val or max_num <= root.val:
                return False
            # 遍历左子树时,此时的最大值应该是根
            if not dfs(root.left, min_num, root.val):
                return False
            # 遍历右子树时,此时的最小值应该是根
            if not dfs(root.right, root.val, max_num):
                return False
            return True
        return dfs(root)
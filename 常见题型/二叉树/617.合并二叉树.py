"""
给两棵树root1和root2,将两棵树合并,从根开始,相同位置上均有元素则相加,有一方无元素则直接填写另一方的元素,都无则为空;
root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7] --> [3,4,5,5,4,null,7]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            # 要是一边不存在,直接返回另一边
            # 这样的目的是防止在下一次dfs时有root为None,无left或right会报错
            if not root1:
                return root2
            if not root2:
                return root1
            root = TreeNode(val = root1.val + root2.val)
            root.left = dfs(root1.left, root2.left)
            root.right = dfs(root1.right, root2.right)
            return root
        return dfs(root1, root2)
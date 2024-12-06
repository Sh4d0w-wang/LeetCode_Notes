"""
给一个根节点root,翻转这棵二叉树,并返回根节点;
root = [4,2,7,1,3,6,9] --> [4,7,2,9,6,3,1]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 层序遍历的同时翻转左孩子和右孩子
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = collections.deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                lc, rc = None, None
                if node.right:
                    rc = node.right
                    queue.append(rc)
                if node.left:
                    lc = node.left
                    queue.append(lc)
                node.left = rc
                node.right = lc
        return root
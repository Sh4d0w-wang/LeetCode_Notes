"""
给一个二叉树的root,找出该二叉树的最底层,最左边的节点值;
root = [2, 1, 3] --> 1
root = [1, 2, 3, 4, null, 5, 6, null, null, 7] --> 7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 层序遍历(从左到右)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res[-1][0]
    # 层序遍历(从右向左,这样就不需要存,直接输出即可)
    def findBottomLeftValue_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
"""
给一个二叉树的root,返回其最大深度;
二叉树的最大深度是指从根节点到最远叶节点的最长路径上的节点数;
root = [3,9,20,null,null,15,7] --> 3
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 解法1
    # 深度优先遍历(本质上是后序遍历)
    def maxDepth_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 先left，再right，最后max()+1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    # 解法2
    # 广度优先搜索(层序遍历)
    def maxDepth_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res
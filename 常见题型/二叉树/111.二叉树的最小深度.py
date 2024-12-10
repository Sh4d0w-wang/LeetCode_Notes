"""
给一个二叉树的根root,返回其最小深度;
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 解法1
    # 层序遍历,若到某一层时遇到了一个节点的左右孩子都空,则就是它的深度为最小
    def minDepth_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        queue = collections.deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth
    # 解法2
    # 深度优先遍历
    def minDepth_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 到达叶节点时返回
        if not root.left and not root.right:
            return 1
        depth = 1e9
        # 一直往下遍历到叶节点,几层就往上加几
        # 途中一直保持最小
        if root.left:
            depth = min(self.minDepth(root.left), depth)
        if root.right:
            depth = min(self.minDepth(root.right), depth)
        return depth + 1
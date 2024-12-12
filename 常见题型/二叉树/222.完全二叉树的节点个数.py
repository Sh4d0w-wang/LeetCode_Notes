"""
给一个完全二叉树的根节点root,求出该树的节点个数;
root = [1, 2, 3, 4, 5, 6] --> 6
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 解法1
    # 层序遍历
    def countNodes_1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        count = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                count += 1
        return count
    # 解法2
    # 递归，也可以说成二分法
    def countNodes_2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)
        return left_count + right_count + 1
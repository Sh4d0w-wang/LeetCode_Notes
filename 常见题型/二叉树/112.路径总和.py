"""
给一个树的root和一个目标和targetSum,判断是否存在根节点到叶子节点上所有节点的和等于targetSum;
存在返回True,没有返回False;
root = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1],targetSum = 22 --> True
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 解法1
    # 深度优先遍历,从上往下
    def hasPathSum_1(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
    # 解法2
    # 广度优先遍历(层序遍历)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = collections.deque()
        # 已经加上该节点的值了
        queue.append((root, root.val))
        while queue:
            node, current_sum = queue.popleft()
            if not node.left and not node.right and current_sum == targetSum:
                return True
            if node.left:
                # 需要加上下一个节点的值
                queue.append((node.left, current_sum + node.left.val))
            if node.right:
                queue.append((node.right, current_sum + node.right.val))
        return False
"""
给二叉树的根节点root,返回层序遍历的序列;
root = [3,9,20,null,null,15,7] --> [[3],[9,20],[15,7]]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp = []
            # 将各个node的子节点均入队
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res
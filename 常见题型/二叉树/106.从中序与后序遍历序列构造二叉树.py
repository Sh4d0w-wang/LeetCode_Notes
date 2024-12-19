"""
给两个数组inorder和postorder,构造并返回这个二叉树;
inorder = [9,3,15,20,7], postorder = [9,15,7,20,3] --> [3,9,20,null,null,15,7]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 当前中序遍历的左右边界
        def inorder_helper(left, right):
            # 左边界大于右边界,返回空节点
            if left > right:
                return None
            # 遍历序列的最后都是根
            root_val = postorder.pop()
            root_index = inorder_hashtable[root_val]
            root = TreeNode(val=root_val)
            # 必须先构建右子树
            # 因为postorder是左右根,先取根的话,后面的顺序依次是右左
            root.right = inorder_helper(root_index + 1, right)
            root.left = inorder_helper(left, root_index - 1)
            return root
        # 此处用哈希表是为了效率,O(1)
        inorder_hashtable = dict()
        for i, val in enumerate(inorder):
            inorder_hashtable[val] = i
        root = inorder_helper(0, len(inorder) - 1)
        return root
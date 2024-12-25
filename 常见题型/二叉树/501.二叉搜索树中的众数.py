"""
给一个含重复值的二叉搜索树(BST)的根节点root,找出并返回BST中的所有众数(即出现频率最高的元素);
如果树中有不止一个众数，可以按任意顺序返回;
root = [1,null,2,2] --> [2]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            inorder_list.append(root.val)
            inorder(root.right)
        if not root:
            return []
        inorder_list = []
        inorder(root)
        
        # 记录前一个元素值
        pre = inorder_list[0]
        # 记录次数
        current_count = 1
        # 记录最大次数
        max_count = 1
        # 记录结果
        res = [pre]
        for i in range(1, len(inorder_list)):
            # 当前和前一个相同,次数+1
            # 不同则将其次数设置为1
            if pre == inorder_list[i]:
                current_count += 1
            else:
                current_count = 1
            # 如果当前次数等于最大
            # 将该值加入到res
            if current_count == max_count:
                res.append(inorder_list[i])
            # 如果当前次数已经大于最大
            # 说明之前加的值都没用了
            # 更新最大值和结果
            if current_count > max_count:
                max_count = current_count
                res = [inorder_list[i]]
            pre = inorder_list[i]
        return res
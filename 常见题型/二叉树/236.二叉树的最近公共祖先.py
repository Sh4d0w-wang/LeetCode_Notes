"""
给定一个二叉树,找到该树中两个指定节点的最近公共祖先;
也就是往上找 最近 的一个公共祖先,可以是节点本身;
root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 --> 3
解释:节点5和节点1的最近公共祖先是节点3
root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4 --> 5
解释:节点5和节点4的最近公共祖先是节点5;因为根据定义最近公共祖先节点可以为节点本身;
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 只有3种情况
    # 1 -> 返回root -> p,q分别在root的左右两侧
    # 2 -> 返回p -> p和q在同侧,且p在q上面
    # 3 -> 返回q -> p和q在同侧,且q在p上面
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1.为空
        # 2.遍历到p或q了,直接返回
        if not root or root == p or root == q:
            return root
        # 遍历左子树
        # 比如遍历到p了,上面返回p,此时left=p,此时会遍历右子树;
        # 有2种情况,1.right为空(说明q在左子树);2.right不为空(说明p和q在root左右两侧)
        left = self.lowestCommonAncestor(root.left, p, q)
        # 遍历右子树
        right = self.lowestCommonAncestor(root.right, p, q)
        # 像上面这种情况,若left=p,由于是从root往下开始的,p在上面,则返回p即可
        if not left and not right:
            return
        if not left:
            return right
        if not right:
            return left
        # left和right均有值
        return root
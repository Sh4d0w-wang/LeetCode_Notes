"""
给一个单链表的头结点head,然后反转它,并返回新的链表;
[1, 2, 3, 4, 5] --> [5, 4, 3, 2, 1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 遍历原链表,新链表利用头插法即可解决
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        while head != None:
            # 当前的第一个节点
            succ = res.next
            temp = ListNode()
            temp.val = head.val
            # 为空则说明刚开始
            if succ == None:
                res.next = temp
            else:
                # 头插法
                temp.next = succ
                res.next = temp
            head = head.next
        return res.next
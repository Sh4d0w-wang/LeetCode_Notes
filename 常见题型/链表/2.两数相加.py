"""
非空链表1:[2->3->4]
非空链表2:[5->6->1]
逆序存的---->数字1:432,数字2:165
求两数相加,以相同的链表形式给出----> 432 + 165 = 597 --> [7->9->5]
除了0,其余任何数最后都不会是0
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 各自取一个节点相加
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = ListNode()
        flag = 0
        while l1 or l2 or flag:
            if l1:
                flag += l1.val
                l1 = l1.next
            if l2:
                flag += l2.val
                l2 = l2.next
            # 引入头节点会方便一点
            # 不然最后会多出一个节点[0, None]
            tail.next = ListNode(flag % 10)
            flag = flag // 10
            tail = tail.next
        # 记得返回头节点的下一个
        return head.next
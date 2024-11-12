"""
给一个单链表head,两两交换它们的节点;
[1, 2, 3, 4] --> [2, 1, 4, 3]
[1, 2, 3] --> [2, 1, 3]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0)
        dummyhead.next = head
        temp = dummyhead
        # 单数个或者没了就不需要操作
        while temp.next != None and temp.next.next != None:
            # 第一个节点
            first = temp.next
            # 第二个节点
            second = temp.next.next
            # 首先指明开头（这样将上一轮和本轮结合起来了）
            # 没有这个的话，后面就会连不起来（比如当只有temp = head时）
            temp.next = second
            # 交换节点
            first.next = second.next
            second.next = first
            # 迭代，需要保持与上一轮一致（当前轮到前一个）
            temp = first
        return dummyhead.next
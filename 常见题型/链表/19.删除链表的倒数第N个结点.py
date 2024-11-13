"""
给一个单链表head,删除倒数第N个结点;
[1, 2, 3, 4], n = 2 --> [1, 2, 4]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 双指针
    # 第一个和第二个指针保持相同的距离，同步向后遍历
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head
        # 1, 2, 3, 4, 5, 6, 7, 8
        #             f        s
        # n = 3，要删6，f是要删的前一个，s是最后一个
        # s - f = 3
        # second向后移指定个数
        while n > 0:
            second = second.next
            n -= 1
        # 若second为None了，就能推出删除的是第一个结点
        if second == None:
            head = head.next
        else:
            # first与second保持同步向后
            while second.next != None:
                second = second.next
                first = first.next
            # del -> first.next
            # tail -> second
            first.next = first.next.next
        return head
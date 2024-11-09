"""
给一个链表头指针head(无头结点)和一个值val,删除链表中值为val的结点,并返回新的头指针;
head = [1, 2, 6, 3, 4, 5, 6], val = 6 --> head = [1, 2, 3, 4, 5]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 解法1
    # 定义头结点
    # 相同则让其指向下一个
    def removeElements_1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyhead = ListNode()
        dummyhead.next = head
        res = dummyhead
        while dummyhead.next != None:
            if dummyhead.next.val == val:
                dummyhead.next = dummyhead.next.next
            # 这边一定要有else，不然出现相同值的情况下，一次处理了2个结点
            else:
                # 不同的情况下，直接往后指
                dummyhead = dummyhead.next
        return res.next
    # 解法2
    # 对原链表进行操作
    def removeElements_2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 处理开头（因为和后面的结点处理方法不一样）
        # 开头是直接向后移动即可（遇到开头全是重复的，就需要用到循环）
        while head != None and head.val == val:
            head = head.next
        if head == None:
            return head
        else:
            # 不能在一开始定义一个res，因为上面的操作是对开头进行处理的，res始终有值
            res = head
            # 中间的节点是head.next = head.next.next
            while head.next != None:
                if head.next.val == val:
                    head.next = head.next.next
                else:
                    head = head.next
            return res
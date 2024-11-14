"""
给一个链表的头结点,返回它里面环链的第一个结点,没有返回None;
[1, 2, 3, 4, 2] --> 2开始
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 解法1
    # 快慢指针
    # 快的每次走两步，慢的每次走一步（必然会相遇），之后推导出距离起点有多少
    # 设环链前节点有a个，环链节点有b个
    # fast = 2 * slow（fast走的步数是slow的两倍）
    # fast = slow + n * b（fast比slow多走了n个环链节点数，都走了slow的路程，但最终相遇是在链中）
    # 上述两式相减，得到slow = n * b（slow走这么多会与fast相遇）
    # 从头开始slow走到链的开头的步数 = a + n * b（链前 + 链中 * n）
    # 而slow已经走了n * b，再让它走 a + n * b - n * b = a就到链的开头了
    # 此时让fast重新为开头，一起往后走a个就行了
    def detectCycle_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while True:
            # fast走两步，slow走一步
            if fast != None and fast.next != None:
                fast = fast.next.next
                slow = slow.next
                # 第一次相遇，说明slow还有a步就到链的开头
                if fast == slow:
                    fast = head
                    break
            else:
                return None
        # while True:
        #     fast = fast.next
        #     slow = slow.next
        #     if fast == slow:
        #         return fast
        # 不能这么写，pos为0的情况下返回的就是1
        # 0    1    2    0
        # l(s)
        #      s    l
        #      l    s    
        # s(l)第一次相遇
        # l(s)将fast重新变为head
        #      l(s)第二次相遇，但是此时的pos为1
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
    
    # 解法2
    # 哈希表法
    def detectCycle_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        has_visited = set()
        temp = head
        while temp != None:
            # 遇到过，则直接返回该结点
            if temp in has_visited:
                return temp
            else:
                # 没遇到过，往里加
                has_visited.add(temp)
                temp = temp.next
        return None
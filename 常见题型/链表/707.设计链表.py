"""
单链表或双链表,有val,next,prev(双链表中);
init():初始化对象;
int get(int index):获取下标为index的值,无效则为-1;
void addAtHead(int val):将val插入到第一个结点之前;
void addAtTail(int val):将val插入到最后一个结点之后;
void addAtIndex(int index, int val):将val插入到index位置,若index等于链表长度,则加到最后,若index长度大于链表长度,则无效;
void deleteAtIndex(int index):删除下标为Index的结点
"""
# 定义结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class MyLinkedList:
    # 初始化链表，引入头结点和尾结点
    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # 为了提高效率，判断它是在前半还是后半
    def get(self, index: int) -> int:
        if index < 0 or self.size <= index:
            return -1
        if index * 2 < self.size:
            temp = self.head
            for _ in range(index + 1):
                temp = temp.next
            return temp.val
        else:
            temp = self.tail
            for _ in range(self.size - index):
                temp = temp.prev
            return temp.val
    
    # 可以直接调用addAtIndex
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
    
    # 可以直接调用addAtIndex
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    
    # 都取index结点到前一个和后一个，统一操作
    def addAtIndex(self, index: int, val: int) -> None:
        if self.size < index or index < 0:
            return
        if index * 2 < self.size:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
        new_node = ListNode(val)
        new_node.next = succ
        new_node.prev = pred
        pred.next = new_node
        succ.prev = new_node
        self.size += 1

    # 都取index结点到前一个和后一个，统一操作
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        if index * 2 < self.size:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
        pred.next = succ
        succ.prev = pred
        self.size -= 1
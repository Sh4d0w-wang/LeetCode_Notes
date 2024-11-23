"""
用两个队列,实现栈的操作;
push:将元素压到栈顶;
pop:移除并返回栈顶元素;
top:返回栈顶元素;
empty:如果栈为空,返回true,否则返回false;
"""
class MyStack:
    def __init__(self):
        # 初始化两个队列
        # 放元素，[1, 2, 3]，从左到右，栈顶--栈底
        self.queue_1 = collections.deque()
        # 过渡矩阵，当新元素push到栈顶，先进入queue2（这样元素pop顶时候是第一个出去），
        # 然后将queue1的元素依次移到queue2的后面，以此实现一个栈
        self.queue_2 = collections.deque()

    def push(self, x: int) -> None:
        self.queue_2.append(x)
        while self.queue_1:
            self.queue_2.append(self.queue_1.popleft())
        self.queue_1, self.queue_2 = self.queue_2, self.queue_1

    # 直接移出队头
    def pop(self) -> int:
        return self.queue_1.popleft()

    def top(self) -> int:
        return self.queue_1[0]

    def empty(self) -> bool:
        return not self.queue_1
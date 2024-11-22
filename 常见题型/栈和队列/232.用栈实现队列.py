"""
用两个栈实现队列
支持:
push:将元素推到队列末尾;
pop:从队列开头移除并返回元素;
peek:返回队列开头元素;
empty:如果队列为空,返回true,否则返回false;
"""
class MyQueue:
    def __init__(self):
        # 左头右尾
        # [1, 2, 3]
        self.stack_a = []
        # 用来rev栈元素
        self.stack_b = []

    # 入队--append--> [1, 2, 3, 4]
    def push(self, x: int) -> None:
        self.stack_a.append(x)
    
    # stack_a依次pop，进入b --> [4, 3, 2, 1]
    # 最上面元素（1）是队头，直接pop即可模拟队列的出队
    def pop(self) -> int:
        # 这边不能self.stack != None
        # if list:  --> 检查list是否为真值,[]在python中被称为假值（即检查list是否存在且有值）
        # if list != None: --> 只检查list是否为None
        # None和空列表不是一回事
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        res = self.stack_b.pop()
        while self.stack_b:
            self.stack_a.append(self.stack_b.pop())
        return res

    # stack_a的第一个元素就是队头
    def peek(self) -> int:
        return self.stack_a[0]

    def empty(self) -> bool:
        if self.stack_a:
            return False
        else:
            return True
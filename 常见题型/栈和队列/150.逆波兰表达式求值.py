"""
给一个字符串数组tokens,表示一个根据逆波兰表示法表示的算术表达式,求出表达式的值;
tokens = ["2","1","+","3","*"] --> ((2 + 1) * 3) = 9
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] --> ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
"""
class Solution:
    def calculate(self, num1:int, num2:int, op:str) -> int:
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return int(num1 / num2)

    # 遇到数字往里push
    # 遇到运算符,从栈中取出两个,并将计算后的结果放进栈
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            try:
                stack.append(int(element))
            except:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calculate(num1, num2, element))
        return stack[0]
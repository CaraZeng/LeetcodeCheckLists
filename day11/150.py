# Evaluate Reverse Polish Notaion
# Key Note:
# 1. if we meet number, put into stack, if we meet operator, take out
# two numbers and do the math, then put the result back into stack.
from operator import add, sub, mul

def div(x, y):
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+': add, '-': sub, '*': mul, '/': div}  # 移到类内
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                number2 = stack.pop()
                number1 = stack.pop()
                stack.append(operators[token](number1, number2))  # 修正访问和顺序
        return stack[0]

#
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                number2 = stack.pop()
                number1 = stack.pop()
                if token == '+':
                    result = number1 + number2
                elif token == '-':
                    result = number1 - number2
                elif token == '*':
                    result = number1 * number2
                elif token == '/':
                    # 题目要求向零截断
                    result = int(number1 / number2)
                stack.append(result)
        return stack[0]

        
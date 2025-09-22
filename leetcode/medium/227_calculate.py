import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def getNum(self, num1, num2, op):
        if op == '/':
            return num1 // num2
        elif op == '*':
            return num1 * num2
        elif op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2

    def calculate(self, s: str) -> int:
        operators = ('+', '-', '*', '/')
        data = []

        curr = ''
        for char in s:
            if char.isdigit():
                curr += char
            elif len(curr) != 0:
                data.append(int(curr))
                curr = ''

            if char in operators:
                data.append(char)

        if len(curr) != 0:
            data.append(int(curr))

        stack = []
        i = 0
        n = len(data)
        while i < n:
            if data[i] == '*':
                i += 1
                val = self.getNum(stack.pop(), data[i], '*')
                stack.append(val)
            elif data[i] == '/':
                i += 1
                val = self.getNum(stack.pop(), data[i], '/')
                stack.append(val)
            else:
                stack.append(data[i])
            i += 1

        data = stack
        stack = []
        i = 0
        n = len(data)
        while i < n:
            if data[i] == '+':
                i += 1
                val = self.getNum(stack.pop(), data[i], '+')
                stack.append(val)
            elif data[i] == '-':
                i += 1
                val = self.getNum(stack.pop(), data[i], '-')
                stack.append(val)
            else:
                stack.append(data[i])
            i += 1

        return stack[0]

def test ():
    params = [

        {
            'input': "1-1+1",
            'output': 1,
        },
        {
            'input': "0-2147483647",
            'output': -2147483647,
        },
        {
            'input': "3+2*2",
            'output': 7,
        },
        {
            'input': " 3/2 ",
            'output': 1,
        },
        {
            'input': " 3+5 / 2 ",
            'output': 5,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.calculate(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()

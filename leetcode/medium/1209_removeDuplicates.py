from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution_0:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        def isOk():
            n = len(stack)
            if n < k:
                return False

            for i in range(n-k, n):
                if stack[i] != stack[-1]:
                    return False

            return True

        for char in s:
            stack.append(char)

            if len(stack) < k:
                continue

            while isOk():
                n = len(stack)
                for i in range(n-k, n):
                    stack.pop()

        return ''.join(stack)


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def rec(string):
            stack = []
            left = -1
            found = False

            for char in string:
                if len(stack) == 0 or stack[-1] != char:
                    stack.append(char)
                    left = len(stack) - 1
                    continue
                else:
                    stack.append(char)

                if len(stack) - left == k:
                    found = True
                    for i in range(k):
                        stack.pop()
                    left = len(stack) - 1

            return ''.join(stack) if not found else rec(''.join(stack))

        return rec(s)

'''
d e e e

'''


def test ():
    params = [
        {
            'input': ["abcd", 2],
            'output': 'abcd',
        },
        {
            'input': ["deeedbbcccbdaa", 3],
            'output': 'aa',
        },
        {
            'input': ["pbbcggttciiippooaais", 2],
            'output': 'ps',
        },
    ]
    solution = Solution()

    for param in params:
        s, k = param['input']
        result = solution.removeDuplicates(s, k)
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

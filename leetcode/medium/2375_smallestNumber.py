import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def smallestNumber_0(self, pattern: str) -> str:
        res = ''
        used = [None]*10

        def rec(text, id):
            nonlocal res, used, pattern

            if id == len(pattern):
                res = text
                return True

            for i in range(1, 10):
                if used[i]:
                    continue

                prev = int(text[-1])
                if pattern[id] == 'I' and prev > i:
                    continue
                if pattern[id] == 'D' and prev < i:
                    break

                used[i] = True
                if rec(text + str(i), id + 1):
                    return True
                used[i] = None

            return False


        for i in range(1, 10):
            used[i] = True
            if rec(str(i), 0):
                return res
            used[i] = None

        return res

    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []

        for i in range(len(pattern) + 1):
            stack.append(i + 1)

            while stack and (i == len(pattern) or pattern[i] == 'I'):
                res.append(str(stack.pop()))

        return ''.join(res)

'''

DDD
1234 = 4321

IIIDIDDD
123
   45=54
     6789=9876
123549876

'''


def test ():
    params = [
        {
            'input': 'IIIDIDDD',
            'output': '123549876',
        },
        {
            'input': 'DDD',
            'output': '4321',
        },
        {
            'input': 'DDID',
            'output': '32154',
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.smallestNumber(param['input'])
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

import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def rangeBitwiseAnd_0(self, left: int, right: int) -> int:
        small = min(left, right)
        big = max(left, right)
        if small == 0:
            return 0

        if big == small:
            return small

        resArr = list(bin(small)[2:])
        resArr.reverse()

        for i in range(1, len(resArr)+1):
            s = '0b'+'1'+'0'*i
            n = int(s, 2)
            if n >= small and n <= big:
                for j in range(i):
                    resArr[j] = '0'

        resArr.reverse()

        return int('0b' + ''.join(resArr), 2)


    def rangeBitwiseAnd_1(self, left: int, right: int) -> int:
        small = min(left, right)
        big = max(left, right)
        if small == 0:
            return 0

        if big == small:
            return small

        smallStr = bin(small)[2:]
        if int('0b1'+'0'*len(smallStr), 2) <= big:
            return 0

        smallStr = '1'*len(smallStr)
        resArr = list(smallStr)

        for i in range(len(smallStr)):
            s = '0b' + smallStr[:i] + '0' + smallStr[i+1:]
            n = int(s, 2)
            if n <= big and n >= small:
                resArr[i] = '0'

        return int('0b'+''.join(resArr), 2)

    def rangeBitwiseAnd_2(self, left: int, right: int) -> int:
        small = min(left, right)
        big = max(left, right)
        if small == 0:
            return 0

        if big == small:
            return small

        smallStr = bin(small)[2:]
        if int('0b1'+'0'*len(smallStr), 2) <= big:
            return 0

        res = small

        visited = set()
        def rec(text, id):
            nonlocal big, small, res, visited

            if id == len(text):
                return

            t1 = text[:id] + '0' + text[id+1:]
            n1 = int('0b' + t1, 2)

            if n1 > small:
                if n1 <= big:
                    res &= n1
                rec(t1, id + 1)

            rec(text, id + 1)

        rec('1'*len(smallStr), 0)

        return res




'''

1 0 1
1 1 1

1 0 1
0 1 1
1 1 1

0 0 1 = 4

---

30
1 1 1 1 0
10
0 1 0 1 0

0 1 0 1 1
0 1 1 0 0
0 1 1 0 1




'''


def test ():
    params = [
        {
            'input': [1073741824, 2147483647],
            'output': 1073741824,
        },
        {
            'input': [9, 10],
            'output': 8,
        },
        {
            'input': [4, 5],
            'output': 4,
        },
        {
            'input': [3,3],
            'output': 3,
        },
        {
            'input': [5,7],
            'output': 4,
        },
        {
            'input': [0, 0],
            'output': 0,
        },
        {
            'input': [1, 2147483647],
            'output': 0,
        },
        {
            'input': [2, 4],
            'output': 0,
        },
        {
            'input': [1, 2],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        left, right = param['input']
        result = solution.rangeBitwiseAnd(left, right)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()

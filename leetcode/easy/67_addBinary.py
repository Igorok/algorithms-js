import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        arr1 = list(a)
        arr1.reverse()

        arr2 = list(b)
        arr2.reverse()

        l1 = len(arr1)
        l2 = len(arr2)
        i = 0
        j = 0
        rem = 0
        res = []

        while i < l1 or j < l2 or rem > 0:
            v1 = 0 if i >= l1 else int(arr1[i])
            v2 = 0 if j >= l2 else int(arr2[j])

            curr = v1 + v2
            if rem:
                curr += rem
                rem -= 1

            rem = curr // 2
            curr = curr % 2

            res.append(str(curr))

            i += 1
            j += 1

        res.reverse()

        return ''.join(res)





def test ():
    params = [
        {
            'input': ["11", "1"],
            'output': '100',
        },
        {
            'input': ["1010", "1011"],
            'output': '10101',
        },
    ]
    solution = Solution()

    for param in params:
        a, b = param['input']
        result = solution.addBinary(a, b)
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

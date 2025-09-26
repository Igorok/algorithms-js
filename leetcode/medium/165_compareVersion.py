import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')

        l1 = len(arr1)
        l2 = len(arr2)
        lm = max(len(arr1), len(arr2))

        for i in range(lm):
            n1 = 0 if i >= l1 else int(arr1[i])
            n2 = 0 if i >= l2 else int(arr2[i])

            if n1 > n2:
                return 1
            elif n1 < n2:
                return -1

        return 0


def test ():
    params = [
        {
            'input': ["1.2", "1.10"],
            'output': -1,
        },
        {
            'input': ["1.01", "1.001"],
            'output': 0,
        },
        {
            'input': ["1.0", "1.0.0.0"],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        version1, version2 = param['input']
        result = solution.compareVersion(version1, version2)
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

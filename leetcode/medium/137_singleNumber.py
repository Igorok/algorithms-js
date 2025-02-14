import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sumOfBits = [0]*33
        minus = 0

        for num in nums:
            if num < 0:
                minus += 1
                num = abs(num)
            i = 0
            while num != 0:
                sumOfBits[i] += (num % 2)
                num = num // 2
                i += 1

        sumOfBits = [str(s%3) for s in sumOfBits]
        sumOfBits.reverse()
        num = int('0b' + ''.join(sumOfBits), 2)

        return -num if (minus % 3) == 1 else num


'''

11
11
1
11

01

---

01
01
01
1

11

---

1
1
01
1

11



'''


def test ():
    params = [
        {
            'input': [2,2,3,2],
            'output': 3,
        },
        {
            'input': [0,1,0,1,0,1,99],
            'output': 99,
        },
        {
            'input': [3,3,1,3],
            'output': 1,
        },
        {
            'input': [2,2,1,2],
            'output': 1,
        },
        {
            'input': [-2,-2,1,1,4,1,4,4,-4,-2],
            'output': -4,
        },
        {
            'input': [-19,-46,-19,-46,-9,-9,-19,17,17,17,-13,-13,-9,-13,-46,-28],
            'output': -28,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.singleNumber(param['input'])
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

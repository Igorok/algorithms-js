from typing import List
import json
from collections import deque
import heapq

class Solution_0:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainders = set()
        acc = 0

        for i in range(k+2):
            acc += 10**i
            if acc % k == 0:
                return i + 1

            if acc in remainders:
                return -1

            remainders.add(acc)

        return -1

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainders = set()
        r = 10 % k
        acc = 1
        num = 1

        for i in range(1, k+3):
            if num % k == 0:
                return i

            acc = (acc * r) % k
            num = (num + acc) % k

            if num in remainders:
                return -1
            remainders.add(num)

        return -1

'''

1 % 3 = 1
* 10
10 % 30 = 10
+1

1 % 3 = 1
11 % 3 = 2
111 % 3 = 0


(a+b)mod = ((a)mod + (b)mod)mod

1/3 = 1%3 + 10**0 = 1
11/3 = (1 + 10**1) / 3 = 2
111/3 = 1/3 + 10/3 + 100/3 =









'''


def test ():
    params = [
        {
            'input': 1,
            'output': 1,
        },
        {
            'input': 2,
            'output': -1,
        },
        {
            'input': 3,
            'output': 3,
        },
        {
            'input': 7,
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        k = param['input']
        result = solution.smallestRepunitDivByK(k)
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

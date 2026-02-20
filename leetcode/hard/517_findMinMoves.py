from typing import List
import json
from collections import deque, defaultdict
import heapq


class Solution_0:
    def findMinMoves(self, machines: List[int]) -> int:
        N = len(machines)
        total = sum(machines)
        avg = total // N

        if total % N != 0:
            return -1

        res = 0

        for i in range(N):
            n = machines[i]
            res = max(res, abs(avg - n))

        return res


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        N = len(machines)
        total = sum(machines)
        avg = total // N

        if total % N != 0:
            return -1

        res = 0
        acc = 0
        for i in range(N):
            n = machines[i]

            if acc <= 0 and n <= avg:
                acc += n - avg
                continue

            if acc >= 0 and n >= avg:
                acc += n - avg
                continue

            if acc > 0 and n < avg:
                diff = avg - n
                move = min(acc, diff)
                res += move
                acc -= diff
                continue

            if acc < 0 and n > avg:
                diff = n - avg
                move = min(abs(acc), diff)
                res += move
                acc += diff
                continue

        return res

'''

0 1 5
-2 -1 5
-1 -1 4
0 -1 3
0 0 2

---

1 0 5
-1 -2 5
-1 -1 4
-1 0 3
0 0 2


---
0,0,11,5
4

-4 -4 +7 +1
0 -1 0 +1

---

5 11 0 0


'''

def test ():
    params = [
        {
            'input': [1,0,5],
            'output': 3,
        },
        {
            'input': [0,3,0],
            'output': 2,
        },
        {
            'input': [0,2,0],
            'output': -1,
        },
        {
            'input': [0,0,11,5],
            'output': 8,
        },
        {
            'input': [4,0,0,4],
            'output': 2,
        },
        {
            'input': [0,0,4,4],
            'output': 4,
        },
        {
            'input': [10, 0, 0, 1, 0, 0, 10],
            'output': 7,
        },
    ]
    solution = Solution()

    for param in params:
        machines = param['input']
        result = solution.findMinMoves(machines)
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

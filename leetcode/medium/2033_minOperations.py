from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        even = (x % 2) == 0
        arr = []
        for i in range(len(grid)):
            for num in grid[i]:
                arr.append(num)

        arr.sort()
        length = len(arr)
        median = length // 2

        res = 0
        for num in arr:
            diff = abs(arr[median] - num)
            if diff % x != 0:
                return -1
            else:
                res += diff // x


        return res

'''


2
2 4 6 8
4 6 6 6 + 3
6 6 6 6 + 1

1
1 2 3 5
2 3 3 4 +3
3 3 3 3 +2

1 2 3 5
(2+3) // 2 = 2






1 2 3 6 6 6 6
30 / 7  4.3

1 2 3 6 6 6 6
2 3 4 5 5 5 5 +7
3 4 4 4 4 4 4 +6
4 4 4 4 4 4 4 +1
+14


1 2 3 6 6 6 6
2 3 4 6 6 6 6 +3
3 4 5 6 6 6 6 +3
4 5 6 6 6 6 6 +3
5 6 6 6 6 6 6 +2
6 6 6 6 6 6 6 +1
+12

1 1 1 3 20 20 20

3
1 1 5 13
1+5/2 = 6

10
2 12 22 32
(12 + 22) // 2 = 17

'''


def test ():
    params = [
        {
            'input': [[[2,4],[6,8]], 2],
            'output': 4,
        },
        {
            'input': [[[1,5],[2,3]], 1],
            'output': 5,
        },
        {
            'input': [[[1,2],[3,4]], 2],
            'output': -1,
        },
        {
            'input': [[[1, 2, 3, 6, 6, 6, 6]], 1],
            'output': 12,
        },
        {
            'input': [[[1, 1, 1, 3, 20, 20, 20]], 1],
            'output': 57,
        },
        {
            'input': [[[1, 1, 5, 13]], 3],
            'output': -1,
        },
        {
            'input': [[[980,476,644,56],[644,140,812,308],[812,812,896,560],[728,476,56,812]], 84],
            'output': 45,
        },
    ]
    solution = Solution()

    for param in params:
        grid, x = param['input']
        result = solution.minOperations(grid, x)
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

from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        cars = sorted(
            [[position[i], speed[i]] for i in range(N)],
            key = lambda x: -x[0]
        )

        res = 0
        pastArrival = -1

        for pos, spd in cars:
            arriveAt = (target - pos) / spd
            if arriveAt > pastArrival:
                res += 1
                pastArrival = arriveAt

        return res

'''
[12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]]

[[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]

12-10 / 2 = 1
12-8 / 4 = 1

12-5 / 1 = 7
12-3 / 3 = 1

12-0 / 1 = 12


'''

def test ():
    params = [
        {
            'input': [12, [10,8,0,5,3], [2,4,1,1,3]],
            'output': 3,
        },
        {
            'input': [10, [3], [3]],
            'output': 1,
        },
        {
            'input': [100, [0,2,4], [4,2,1]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        target, position, speed = param['input']
        result = solution.carFleet(target, position, speed)
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

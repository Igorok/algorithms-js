
from typing import List
import json
from collections import Counter
from functools import cache

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # dist / time = speed
        # time = dist / steed
        N = len(dist)
        times = sorted([dist[i] / speed[i] for i in range(N)])


        res = 0
        curr = 0
        for t in times:
            if t <= curr:
                return res
            res += 1
            curr += 1

        return res


def test ():
    params = [
        {
            'input': [[1,3,4], [1,1,1]],
            'output': 3,
        },
        {
            'input': [[1,1,2,3], [1,1,1,1]],
            'output': 1,
        },
        {
            'input': [[3,2,4], [5,3,2]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        dist, speed = param['input']
        result = solution.eliminateMaximum(dist, speed)
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

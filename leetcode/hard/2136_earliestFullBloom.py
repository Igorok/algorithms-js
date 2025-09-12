from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        return 0


def test ():
    params = [
        {
            'input': [[1,4,3], [2,3,1]],
            'output': 9,
        },
        {
            'input': [[1,2,3,2], [2,1,2,1]],
            'output': 9,
        },
        {
            'input': [[1], [1]],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        plantTime, growTime = param['input']
        result = solution.earliestFullBloom(plantTime, growTime)
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

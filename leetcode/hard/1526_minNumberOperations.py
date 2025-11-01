from typing import List
import json
from collections import deque, defaultdict


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        curr = 0

        for num in target:
            if curr >= num:
                curr = num
                continue

            if curr < num:
                diff = num - curr
                res += diff
                curr += diff

        return res

def test ():
    params = [
        {
            'input': [1,2,3,2,1],
            'output': 3,
        },
        {
            'input': [3,1,1,2],
            'output': 4,
        },
        {
            'input': [3,1,5,4,2],
            'output': 7,
        },
    ]
    solution = Solution()

    for param in params:
        target = param['input']
        result = solution.minNumberOperations(target)
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

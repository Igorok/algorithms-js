from typing import List
import json
from collections import deque

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        return 0

def test ():
    params = [
        {
            'input': [[3,1,1],[2,5,1],[1,5,5],[2,1,1]],
            'output': 24,
        },
        {
            'input': [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]],
            'output': 28,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.cherryPickup(param['input'])
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

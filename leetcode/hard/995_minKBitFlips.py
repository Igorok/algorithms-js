from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        return -1

'''

1 1 0 1 1 0 0
0 0 1 0 0

'''



def test ():
    params = [
        {
            'input': [[0,1,0], 1],
            'output': 2,
        },
        {
            'input': [[1,1,0], 2],
            'output': -1,
        },
        {
            'input': [[0,0,0,1,0,1,1,0], 3],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.minKBitFlips(nums, k)
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

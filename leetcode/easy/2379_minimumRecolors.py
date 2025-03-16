from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = float('inf')
        bCount = 0
        for i in range(k):
            if blocks[i] == 'B':
                bCount += 1

        if bCount >= k:
            return 0
        else:
            res = k - bCount

        n = len(blocks)
        for i in range(1, n-k+1):
            if blocks[i-1] == 'B':
                bCount -= 1
            if blocks[i+k-1] == 'B':
                bCount += 1

            res = min(res, k - bCount)

        return res


def test ():
    params = [
        {
            'input': ["WBBWWBBWBW", 7],
            'output': 3,
        },
        {
            'input': ["WBWBBBW", 2],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        blocks, k = param['input']
        result = solution.minimumRecolors(blocks, k)
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

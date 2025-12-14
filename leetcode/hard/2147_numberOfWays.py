from typing import List
import json
from collections import deque
import heapq
import math


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 7 + 10**9
        N = len(corridor)
        memo = [0] * math.ceil(N/2)

        local = 1
        cnt = 0

        for i in range(N):
            if corridor[i] == 'P':
                if cnt % 2 == 1:
                    continue
                if cnt // 2 == 0:
                    local = 1
                else:
                    local += 1
            else:
                cnt += 1
                if cnt % 2 == 1:
                    prevId = cnt//2 - 1
                    prevComb = 1 if prevId == -1 else memo[prevId]
                    memo[cnt//2] = (local * prevComb) % MOD
                else:
                    local = 1

        # print('memo', memo)


        if cnt % 2 == 1:
            return 0

        return memo[cnt // 2 - 1]

'''

SSPPSSPPSSPP
012333699999

'''


def test ():
    params = [
        {
            'input': 'SSPPSPS',
            'output': 3,
        },
        {
            'input': 'PPSPSP',
            'output': 1,
        },
        {
            'input': 'S',
            'output': 0,
        },
        {
            'input': 'SSPPSSPPSSPP',
            'output': 9,
        },
    ]
    solution = Solution()

    for param in params:
        corridor = param['input']
        result = solution.numberOfWays(corridor)
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

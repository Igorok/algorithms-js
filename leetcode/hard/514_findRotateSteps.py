import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        N = len(key)
        M = len(ring)

        cache = []
        for i in range(M):
            row = []
            for j in range(N):
                row.append([float('inf')] * 2)
            cache.append(row)

        def dfs(pos, id, direction):
            nonlocal key, N, M

            if id == N:
                return 0

            if cache[pos][id][direction] != float('inf'):
                return cache[pos][id][direction]

            if key[id] != ring[pos]:
                nextPos = pos
                if direction == 0:
                    nextPos = (pos + 1) % M
                else:
                    nextPos = pos - 1 if pos > 0 else M - 1
                return 1 + dfs(nextPos, id, direction)

            res = 1
            res += min(
                dfs(pos, id+1, 0),
                dfs(pos, id+1, 1),
            )

            cache[pos][id][direction] = res

            return res


        res = min(dfs(0, 0, 0), dfs(0, 0, 1))

        return res


def test ():
    params = [
        {
            'input': ["godding",  "gd"],
            'output': 4,
        },
        {
            'input': ["godding", "godding"],
            'output': 13,
        },
    ]
    solution = Solution()

    for param in params:
        ring, key = param['input']
        result = solution.findRotateSteps(ring, key)
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

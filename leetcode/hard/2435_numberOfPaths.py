from typing import List
import json
from collections import deque
import heapq

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        M = len(grid)
        N = len(grid[0])
        MOD = 7+10**9
        KMAX = k+2

        memo = []
        for r in range(M):
            memo.append([])
            for c in range(N):
                memo[-1].append([0]*KMAX)
                grid[r][c] = grid[r][c] % k

        memo[0][0][grid[0][0]] = 1

        for r in range(M):
            for c in range(N):
                if r == 0 and c == 0:
                    continue

                top = [0]*KMAX if r == 0 else memo[r-1][c]
                left = [0]*KMAX if c == 0 else memo[r][c-1]

                for i in range(KMAX):
                    if top[i] != 0:
                        rem = (i + grid[r][c]) % k
                        memo[r][c][rem] = (top[i] + memo[r][c][rem]) % MOD

                    if left[i] != 0:
                        rem = (i + grid[r][c]) % k
                        memo[r][c][rem] = (left[i] + memo[r][c][rem]) % MOD

        return memo[-1][-1][0]


'''
[[[2, 2, 1], [0, 0, 2], [0, 1, 2]], 3]

[[
[5,2,4],
[3,0,5],
[0,7,2]
]

[
[2, 2, 1],
[0, 0, 2],
[0, 1, 2]
]

[
[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
[[1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
[[2, 2, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
]



'''

def test ():
    params = [
        {
            'input': [[[5,2,4],[3,0,5],[0,7,2]], 3],
            'output': 2,
        },
        {
            'input': [[[0,0]], 5],
            'output': 1,
        },
        {
            'input': [[[7,3,4,9],[2,3,6,2],[2,3,7,0]], 1],
            'output': 10,
        },
    ]
    solution = Solution()

    for param in params:
        grid, k = param['input']
        result = solution.numberOfPaths(grid, k)
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

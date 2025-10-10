from typing import List
from json import dumps
from collections import defaultdict, deque
import heapq


class Solution_0:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        memo = [None] * n

        def dfs(id):
            if id >= n:
                return 0

            if memo[id] != None:
                return memo[id]

            memo[id] = energy[id] + dfs(id + k)

            return memo[id]

        res = float('-inf')

        for i in range(n):
            r = dfs(i)
            res = max(res, r)

        return res


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        memo = [0] * n
        res = float('-inf')

        for i in range(n-1, -1, -1):
            prev = 0 if i + k >= n else memo[i+k]
            memo[i] = energy[i] + prev
            res = max(res, memo[i])

        return res

def test ():
    params = [
        {
            'input': [
                [5,2,-10,-5,1], 3,
            ],
            'output': 3,
        },
        {
            'input': [
                [-2,-3,-1], 2
            ],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        energy, k = param['input']
        result = solution.maximumEnergy(energy, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()

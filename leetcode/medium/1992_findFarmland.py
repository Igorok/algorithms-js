from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        shifts = ((-1, 0), (1, 0), (0, -1), (0, 1))
        n = len(land)
        m = len(land[0])

        def dfs(r, c, id):
            land[r][c] = id

            data = [r, c, r, c]

            for sR, sC in shifts:
                newR = r + sR
                newC = c + sC

                if newR < 0 or newR == n or newC < 0 or newC == m or land[newR][newC] != 1:
                    continue

                res = dfs(newR, newC, id)

                if (res[0] <= data[0] and res[1] <= data[1]):
                    data[0] = res[0]
                    data[1] = res[1]

                if (res[2] >= data[2] and res[3] >= data[3]):
                    data[2] = res[2]
                    data[3] = res[3]

            return data


        id = 2
        res = []
        for r in range(n):
            for c in range(m):
                if land[r][c] == 1:
                    data = dfs(r, c, id)
                    res.append(data)
                    id += 1

        return res

def test ():
    params = [
        {
            'input': [[1,0,0],[0,1,1],[0,1,1]],
            'output': [[0,0,0,0],[1,1,2,2]],
        },
        {
            'input': [[1,1],[1,1]],
            'output': [[0,0,1,1]],
        },
        {
            'input': [[0]],
            'output': [],
        },
    ]
    solution = Solution()

    for param in params:
        land = param['input']
        result = solution.findFarmland(land)
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

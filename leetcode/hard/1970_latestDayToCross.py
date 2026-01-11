from typing import List
import json
import heapq
from collections import defaultdict, deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        topKey = (-1, -1)
        bottomKey = (10**6, 10**6)

        parents = {}
        parents[topKey] = { 'p': topKey, 'c': 1, 'k': topKey }
        parents[bottomKey] = { 'p': bottomKey, 'c': 1, 'k': bottomKey }

        def getParent(key):
            if key not in parents:
                parents[key] = { 'p': key, 'c': 1, 'k': key }
                return parents[key]

            node = parents[key]
            if node['p'] == node['k']:
                return node

            parent = getParent(node['p'])

            if node['p'] != parent['k']:
                parents[key]['p'] = parent['k']

            return parent

        def setParent(key1, key2):
            parent1 = getParent(key1)
            parent2 = getParent(key2)

            if parent1['k'] == parent2['k']:
                return

            if parent1['c'] < parent2['c']:
                parent1['p'] = parent2['k']
                parent2['c'] += parent1['c']
            else:
                parent2['p'] = parent1['k']
                parent1['c'] += parent2['c']


        matrix = [[0] * col for i in range(row)]
        N = len(cells)
        for i in range(N):
            cells[i][0] -= 1
            cells[i][1] -= 1
            r, c = cells[i]
            matrix[r][c] = 1

        def dfs(r, c):
            shifts = ((1,0), (-1, 0), (0, 1), (0, -1))

            for sR, sC in shifts:
                newR = r + sR
                newC = c + sC
                if newR < 0 or newR == row or newC < 0 or newC == col:
                    continue
                if matrix[newR][newC] == 1:
                    continue

                parent1 = getParent((r, c))
                parent2 = getParent((newR, newC))

                if parent1['k'] == parent2['k']:
                    continue

                setParent((r, c), (newR, newC))

                dfs(newR, newC)


        for c in range(col):
            if matrix[0][c] == 0:
                setParent(topKey, (0, c))
                dfs(0, c)
            if matrix[row-1][c] == 0:
                setParent(bottomKey, (row-1, c))
                dfs(row-1, c)

        parent1 = getParent(topKey)
        parent2 = getParent(bottomKey)
        if parent1['k'] == parent2['k']:
            return len(cells)

        for day in range(len(cells)-1, -1, -1):
            r, c = cells[day]
            matrix[r][c] = 0

            if r == row-1:
                setParent(bottomKey, (r, c))
            if r == 0:
                setParent(topKey, (r, c))
            dfs(r, c)

            # print(
            #     'day', day,
            #     'matrix', matrix,
            #     'parents', parents,
            # )

            parent1 = getParent(topKey)
            parent2 = getParent(bottomKey)
            if parent1['k'] == parent2['k']:
                return day



        return 0




def test ():
    params = [
        {
            'input': [2, 2, [[1,1],[2,1],[1,2],[2,2]]],
            'output': 2,
        },
        {
            'input': [2, 2, [[1,1],[1,2],[2,1],[2,2]]],
            'output': 1,
        },
        {
            'input': [
                3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
            ],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        row, col, cells = param['input']
        result = solution.latestDayToCross(row, col, cells)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

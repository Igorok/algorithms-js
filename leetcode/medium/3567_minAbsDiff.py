from typing import List
from json import dumps
from collections import deque
import heapq

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        N = len(grid)
        M = len(grid[0])

        res = []

        for row in range(N-k+1):
            res.append([])

            for col in range(M-k+1):
                if k == 1:
                    res[row].append(0)
                    continue

                unique = set()
                for i in range(k):
                    for j in range(k):
                        unique.add(grid[row+i][col+j])

                if len(unique) == 1:
                    res[row].append(0)
                    continue

                unique = sorted(unique)
                val = float('inf')


                for i in range(1, len(unique)):
                    val = min(val, unique[i] - unique[i-1])

                res[row].append(val)


        return res


'''

[
[
[1,-2, 3],
[2, 3, 5]
],
2
],



'''



def test ():
    params = [
        {
            'input': [[[1,8],[3,-2]], 2],
            'output': [[2]],
        },
        {
            'input': [[[3,-1]], 1],
            'output': [[0,0]],
        },
        {
            'input': [[[1,-2,3],[2,3,5]], 2],
            'output': [[1,2]],
        },
        {
            'input': [
                [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],
                5
            ],
            'output': [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]],
        },
    ]
    solution = Solution()

    for param in params:
        grid, k = param['input']
        result = solution.minAbsDiff(grid, k)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

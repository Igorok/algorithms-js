from typing import List
from json import dumps


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        rl = len(grid) - 2
        result = [[None]*rl for i in range(rl)]

        def getMax(y, x):
            first = grid[y][x]
            yb = min(y + 3, length)
            xr = min(x + 3, length)
            for i in range(y, yb):
                for j in range(x, xr):
                    first = max(first, grid[i][j])

            return first

        for i in range(rl):
            for j in range(rl):
                result[i][j] = getMax(i, j)

        return result


def test ():
    params = [
        {
            'input': [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]],
            'output': [[9,9],[8,6]],
        },
        {
            'input': [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]],
            'output': [[2,2,2],[2,2,2],[2,2,2]],
        },
    ]

    solution = Solution()
    for param in params:
        result = solution.largestLocal(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

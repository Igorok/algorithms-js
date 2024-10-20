from typing import List
from json import dumps


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = {}
        columns = {}

        for i in range(len(grid)):
            row = '_'.join(str(n) for n in grid[i])
            cr = rows.get(row, 0)
            rows[row] = cr + 1

            col = '_'.join(str(grid[j][i]) for j in range(len(grid)))
            cc = columns.get(col, 0)
            columns[col] = cc + 1

        res = 0
        for row, count in rows.items():
            if row in columns:
                c = columns[row]
                res += count * c

        return res

def test ():
    params = [
        {
            'input': [[3,2,1],[1,7,6],[2,7,7]],
            'output': 1,
        },
        {
            'input': [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.equalPairs(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

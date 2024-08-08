from typing import List
import json

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:



        return []


def test ():
    params = [
        {
            'input': [1, 4, 0, 0],
            'output': [[0,0],[0,1],[0,2],[0,3]],
        },
        {
            'input': [5, 6, 1, 4],
            'output': [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]],
        },
    ]
    solution = Solution()

    for param in params:
        rows, cols, rStart, cStart = param['input']
        result = solution.spiralMatrixIII(rows, cols, rStart, cStart)
        print(
            'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

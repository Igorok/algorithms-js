from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rowsCount = len(points)
        columnsCount = len(points[0])

        lastRow = points[0]
        for i in range(1, rowsCount):
            currentRow = points[i].copy()
            rowL = [0] * columnsCount
            rowR = [0] * columnsCount

            rowL[0] = lastRow[0]
            for c in range(1, columnsCount):
                rowL[c] = max(rowL[c - 1] - 1, lastRow[c])

            rowR[-1] = lastRow[-1]
            for c in range(columnsCount - 2, -1, -1):
                rowR[c] = max(rowR[c + 1] - 1, lastRow[c])

            lastRow = [currentRow[c] + max(rowL[c], rowR[c]) for c in range(columnsCount)]

        return max(lastRow)


def test ():
    params = [
        {
            'input': [[1,2,3],[1,5,1],[3,1,1]],
            'output': 9,
        },
        {
            'input': [[1,5],[2,3],[4,2]],
            'output': 11,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.maxPoints(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

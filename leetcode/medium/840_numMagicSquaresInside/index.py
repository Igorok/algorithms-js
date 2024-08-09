from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        countSquares = 0

        def checkAllSums (i, j):
            distinct = set()
            rowSum = [0]*3
            colSum = [0]*3
            diagSum = [0]*2

            for row in range(0, 3):
                distinct.add(grid[i + row][j])
                distinct.add(grid[i + row][j + 1])
                distinct.add(grid[i + row][j + 2])
                if not (1 <= grid[i + row][j] <= 9 and 1 <= grid[i + row][j + 1] <= 9 and 1 <= grid[i + row][j + 2] <= 9):
                    return False

                rowSum[row] = grid[i + row][j] + grid[i + row][j + 1] + grid[i + row][j + 2]
                if rowSum[row] != rowSum[0]:
                    return False

            if len(distinct) < 9:
                return False

            for col in range(0, 3):
                colSum[col] = grid[i][j + col] + grid[i + 1][j + col] + grid[i + 2][j + col]
                if colSum[col] != rowSum[0]:
                    return False

            diagSum[0] = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
            if diagSum[0] != rowSum[0]:
                return False
            diagSum[1] = grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]
            if diagSum[0] != rowSum[0]:
                return False

            return True

        for i in range(0, len(grid) - 2):
            for j in range(0, len(grid[0]) - 2):
                if checkAllSums(i, j):
                    countSquares += 1

                # print('rowSum', rowSum)
                # print('colSum', colSum)
                # print('diagSum', diagSum)
                # print('checkAllSums', checkAllSums())

        return countSquares


def test ():
    params = [
        {
            'input': [[4,3,8,4],[9,5,1,9],[2,7,6,2]],
            'output': 1,
        },
        {
            'input': [[8]],
            'output': 0,
        },
        {
            'input': [[5,5,5],[5,5,5],[5,5,5]],
            'output': 0,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.numMagicSquaresInside(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

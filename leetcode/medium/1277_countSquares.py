from typing import List

class Solution:
    def countSquares_1(self, matrix: List[List[int]]) -> int:
        res = 0
        def checkMatrix(y, x):
            nonlocal matrix, res
            steps = min(len(matrix) - y, len(matrix[0]) - x) + 1
            for step in range(1, steps):
                for i in range(y, y + step):
                    for j in range(x, x + step):
                        if matrix[i][j] == 0:
                            return
                res += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                checkMatrix(i, j)

        return res

    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        memo = [[0]*len(matrix[0]) for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                if val == 0:
                    continue
                x = memo[i][j-1] if j > 0 else 0
                y = memo[i-1][j] if i > 0 else 0
                d = memo[i-1][j-1] if i > 0 and j > 0 else 0
                minSqr = min([x, y, d])
                memo[i][j] = minSqr + 1
                res += memo[i][j]

        return res


def test ():
    params = [
        {
            'input': [
              [0,1,1,1],
              [1,1,1,1],
              [0,1,1,1]
            ],
            'output': 15,
        },
        {
            'input': [
              [1,0,1],
              [1,1,0],
              [1,1,0]
            ],
            'output': 7,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.countSquares(param['input'])

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

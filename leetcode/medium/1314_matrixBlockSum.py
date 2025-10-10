from typing import List
from json import dumps
import heapq


class Solution_1:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                top = max(0, i - k)
                bottom = min(n - 1, i + k)
                left = max(0, j - k)
                right = min(m - 1, j + k)

                for r in range(top, bottom + 1):
                    for c in range(left, right + 1):
                        res[i][j] += mat[r][c]

        return res


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        memo = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                top = 0 if i == 0 else memo[i-1][j]
                left = 0 if j == 0 else memo[i][j-1]
                diag = 0 if i == 0 or j == 0 else memo[i-1][j-1]
                memo[i][j] = mat[i][j] + left + top - diag


        res = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                top = max(0, i - k)
                bottom = min(n - 1, i + k)
                left = max(0, j - k)
                right = min(m - 1, j + k)

                removeBottom = 0 if top == 0 else memo[top-1][right]
                removeLeft = 0 if left == 0 else memo[bottom][left-1]
                addDiag = 0 if top == 0 or left == 0 else memo[top-1][left-1]
                res[i][j] = memo[bottom][right] - removeBottom - removeLeft + addDiag


        return res

'''
i - k <= r <= i + k,
j - k <= c <= j + k

1
[
[1,2,3],
[4,5,6],
[7,8,9]
]

0-1=-1; 0+1=1; -1 <= r <= 1; 0-1=-1; 0+1=1; -1 <= c <= 1;

1, 3,  6
5, 12, 21



'''


def test ():
    params = [
        {
            'input': [
                [[1,2,3],[4,5,6],[7,8,9]],
                1
            ],
            'output': [[12,21,16],[27,45,33],[24,39,28]],
        },
        {
            'input': [
                [[1,2,3],[4,5,6],[7,8,9]],
                2
            ],
            'output': [[45,45,45],[45,45,45],[45,45,45]],
        },
    ]
    solution = Solution()

    for param in params:
        mat, k = param['input']
        result = solution.matrixBlockSum(*param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()

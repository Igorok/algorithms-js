from typing import List
from json import dumps
from collections import deque
import heapq


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        N = len(mat)
        M = len(mat[0])

        shift = k % M
        memo = []

        for row in range(N):
            memo.append([0]*M)

            for col in range(M):
                if col % 2 == 0:
                    if col - shift >= 0:
                        memo[row][col - shift] = mat[row][col]
                        if memo[row][col - shift] != mat[row][col - shift]:
                            return False
                    else:
                        memo[row][M - shift + col] = mat[row][col]
                        if memo[row][M - shift + col] != mat[row][M - shift + col]:
                            return False
                else:
                    memo[row][(col + k) % M] = mat[row][col]
                    if memo[row][(col + k) % M] != mat[row][(col + k) % M]:
                        return False

        return True



def test ():
    params = [
        {
            'input': [[[1,2,3],[4,5,6],[7,8,9]], 4],
            'output': False,
        },
        {
            'input': [[[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2],
            'output': True,
        },
        {
            'input': [[[2,2],[2,2]], 3],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        mat, k = param['input']
        result = solution.areSimilar(mat, k)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()

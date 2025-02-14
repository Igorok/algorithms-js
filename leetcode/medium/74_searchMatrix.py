from typing import List
from json import dumps
import heapq
from collections import deque

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchInRow(row):
            start = 0
            end = len(matrix[row])

            while start <= end:
                m = (start + end) // 2
                if matrix[row][m] == target:
                    return True
                elif matrix[row][m] < target:
                    start = m + 1
                else:
                    end = m - 1

            return False

        start = 0
        end = len(matrix)-1

        while start <= end:
            m = (start + end) // 2

            if matrix[m][0] <= target and matrix[m][-1] >= target:
                return searchInRow(m)
            elif matrix[m][-1] < target:
                start = m + 1
            else:
                end = m - 1

        return False

def test ():
    params = [
        {
            'input': [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3],
            'output': True,
        },
        {
            'input': [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        matrix, target = param['input']
        result = solution.searchMatrix(matrix, target)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
